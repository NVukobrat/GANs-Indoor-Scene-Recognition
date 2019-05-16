import os
import time

import tensorflow as tf
from tensorflow.python import keras
from tensorflow.python.keras import layers
from matplotlib import pyplot as plt

from api import dataset

# Noise size for the input of the Generator model.
GEN_NOISE_INPUT_SHAPE = 100

# Defines interval for saving checkpoints based on epochs.
CKPT_SAVE_INTERVAL = 15


def generator():
    """
    Purpose of the Generator model is to images that looks real. During training,
    the Generator progressively becomes better at creating images that look real.

    The Generator model does upsampling to produces images from random noise. It
    takes random noise as an input, then upsamples several times until reach
    desired image size (in this case 28x28x1).

    :return: The Generator model.
    """
    model = keras.Sequential([
        layers.Dense(units=7 * 7 * 256, use_bias=False, input_shape=(GEN_NOISE_INPUT_SHAPE,)),
        layers.BatchNormalization(),
        layers.LeakyReLU(),
        layers.Reshape((7, 7, 256)),

        layers.Conv2DTranspose(filters=128, kernel_size=(5, 5), strides=(1, 1), padding="same", use_bias=False),
        layers.BatchNormalization(),
        layers.LeakyReLU(),

        layers.Conv2DTranspose(filters=64, kernel_size=(5, 5), strides=(2, 2), padding="same", use_bias=False),
        layers.BatchNormalization(),
        layers.LeakyReLU(),

        layers.Conv2DTranspose(filters=1, kernel_size=(5, 5), strides=(2, 2), padding="same", use_bias=False,
                               activation="tanh"),
    ])

    return model


def generator_loss(fake_output):
    """
    The generator's loss quantifies how well it was able to
    trick the discriminator. Intuitively, if the generator
    is performing well, the discriminator will classify the
    fake images as real (or 1).

    :param fake_output: Fake image produced by Generator model.
    :return: Loss of the Generator.
    """
    cross_entropy = keras.losses.BinaryCrossentropy(from_logits=True)

    return cross_entropy(tf.ones_like(fake_output), fake_output)


def generator_optimizer():
    """
    The Generator model and the Discriminator model uses different
    optimizers because tow different networks are trained.

    :return: Generator optimizer.
    """
    return tf.optimizers.Adam(1e-4)


def discriminator():
    """
    Purpose of the Discriminator model is to learn to tell real images
    apart from fakes. During training, the Discriminator progressively
    becomes better at telling fake images from real ones. The process
    reaches equilibrium when the Discriminator can no longer distinguish
    real images from fakes.

    The Discriminator is a simple CNN-based image classifier. It outputs
    positive values for real images, and negative values for fake images.

    :return: The Discriminator model.
    """
    model = keras.Sequential([
        layers.Conv2D(filters=64, kernel_size=(5, 5), strides=(2, 2), padding='same', input_shape=[28, 28, 1]),
        layers.LeakyReLU(),
        layers.Dropout(rate=0.3),

        layers.Conv2D(filters=128, kernel_size=(5, 5), strides=(2, 2), padding='same'),
        layers.LeakyReLU(),
        layers.Dropout(rate=0.3),

        layers.Flatten(),
        layers.Dense(units=1),
    ])

    return model


def discriminator_loss(real_output,
                       fake_output):
    """
    This method quantifies how well the discriminator is able to distinguish
    real images from fakes. It compares the discriminator's predictions
    on real images to an array of 1s, and the discriminator's predictions
    on fake (generated) images to an array of 0s.

    :param real_output: Real image from dataset.
    :param fake_output: Fake image produced by Generator model.

    :return: Total loss of the Discriminator.
    """
    cross_entropy = keras.losses.BinaryCrossentropy(from_logits=True)

    real_loss = cross_entropy(tf.ones_like(real_output), real_output)
    fake_loss = cross_entropy(tf.zeros_like(fake_output), fake_output)
    total_loss = real_loss + fake_loss

    return total_loss


def discriminator_optimizer():
    """
    The Generator model and the Discriminator model uses different
    optimizers because tow different networks are trained.

    :return: Discriminator optimizer.
    """
    return tf.optimizers.Adam(1e-4)


def define_checkpoint(gen_model,
                      gen_optimizer,
                      dis_model,
                      dis_optimizer):
    """
    Saves and restores (if needed) checkpoints.

    :param gen_model: Generator model.
    :param gen_optimizer: Generator optimizer.
    :param dis_model: Discriminator model.
    :param dis_optimizer: Discriminator optimizer.

    :return: Checkpoint object, Checkpoint name prefix.
    """
    checkpoint_dir = 'res/training_checkpoints'
    checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
    checkpoint = tf.train.Checkpoint(generator_optimizer=gen_optimizer,
                                     discriminator_optimizer=dis_optimizer,
                                     generator=gen_model,
                                     discriminator=dis_model)
    checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))

    return checkpoint, checkpoint_prefix


def train(real_image_dataset,
          last_epoch,
          epochs,
          gen_model,
          gen_optimizer,
          dis_model,
          dis_optimizer,
          checkpoint,
          checkpoint_prefix):
    """
    Train the Generator and Discriminator simultaneously. At the
    beginning of the training, the generated images look like
    random noise. As training progresses, the generated digits
    will look increasingly real. During training process, generated
    images and checkpoints are stored on disk.

    :param real_image_dataset: Dataset that contains real images.
    :param last_epoch: If checkpoint is used, what was the
    last proceed epoch.
    :param epochs: How many epochs should model run.
    :param gen_model: Generator model.
    :param gen_optimizer: Generator optimizer.
    :param dis_model: Discriminator model.
    :param dis_optimizer: Discriminator optimizer.
    :param checkpoint: Checkpoint object.
    :param checkpoint_prefix: Checkpoint name prefix.
    """
    seed = tf.random.normal([16, GEN_NOISE_INPUT_SHAPE])

    for epoch in range(last_epoch, epochs):
        start = time.time()

        for image_batch in real_image_dataset:
            train_step(image_batch, gen_model, gen_optimizer, dis_model, dis_optimizer)

        save_image(gen_model,
                   epoch + 1,
                   seed)

        if (epoch + 1) % CKPT_SAVE_INTERVAL == 0:
            checkpoint.save(file_prefix=checkpoint_prefix)

        print('Time for epoch {} is {} sec'.format(epoch + 1, time.time() - start))

    save_image(gen_model,
               epochs,
               seed)


@tf.function
def train_step(images,
               gen_model,
               gen_optimizer,
               dis_model,
               dis_optimizer):
    """
    The training loop begins with generator receiving a random seed as input.
    That seed is used to produce an image. The discriminator is then used
    to classify real images (drawn from the training set) and fakes
    images (produced by the generator). The loss is calculated for each
    of these models, and the gradients are used to update the generator
    and discriminator.

    The tf.function annotation causes this function to be compiled. This
    allows the TensorFlow runtime to apply optimizations and exploit
    parallelism during the computation. Some reasons not to use this
    annotation:
      - Variables need to be created each time the function is called.
      - You want dynamic Python control flow inside of the function
      (ie, that should change each time you call the function based
      on criteria not passed to the function as args/kwargs).

    :param images: Real image batch.
    :param gen_model: Generator model.
    :param gen_optimizer: Generator optimizer.
    :param dis_model: Discriminator model.
    :param dis_optimizer: Discriminator optimizer.
    """
    noise = tf.random.normal([dataset.BATCH_SIZE, GEN_NOISE_INPUT_SHAPE])

    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generated_images = gen_model(noise, training=True)

        real_output = dis_model(images, training=True)
        fake_output = dis_model(generated_images, training=True)

        gen_loss = generator_loss(fake_output)
        disc_loss = discriminator_loss(real_output, fake_output)

    gradients_of_generator = gen_tape.gradient(gen_loss, gen_model.trainable_variables)
    gradients_of_discriminator = disc_tape.gradient(disc_loss, dis_model.trainable_variables)

    gen_optimizer.apply_gradients(zip(gradients_of_generator, gen_model.trainable_variables))
    dis_optimizer.apply_gradients(zip(gradients_of_discriminator, dis_model.trainable_variables))


def save_image(gen_model,
               epoch,
               test_input):
    """
    Stores generated image examples during the training
    process.

    :param gen_model: Generator model.
    :param epoch: Current epoch.
    :param test_input: Generated image.
    """
    predictions = gen_model(test_input, training=False)

    fig = plt.figure(figsize=(4, 4))

    for i in range(predictions.shape[0]):
        plt.subplot(4, 4, i + 1)
        plt.imshow(predictions[i, :, :, 0] * 127.5 + 127.5, cmap='gray')
        plt.axis('off')

    plt.savefig('res/image_at_epoch_{:04d}.png'.format(epoch))
    plt.close(fig)
