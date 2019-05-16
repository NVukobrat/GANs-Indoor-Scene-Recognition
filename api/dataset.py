import os

import tensorflow as tf
from tensorflow.python import keras

# Full length of the dataset.
BUFFER_SIZE = 60000

# Training batch size.
BATCH_SIZE = 256


def load_normalized_dataset(path):
    """
    Loads dataset,  normalizes it to [-1, +1] values,
    and shuffles.

    Arguments:
        path: The relative path to the dataset.

    Returns:
        The normalized dataset.
    """
    image_samples_path = list()
    for class_dir in os.listdir(path):
        full_class_dir = os.path.join(path, class_dir)
        for image_name in os.listdir(full_class_dir):
            full_image_name = os.path.join(full_class_dir, image_name)
            image_samples_path.append(full_image_name)

    scene_dataset = tf.data.Dataset.from_tensor_slices(
        image_samples_path
    )

    scene_dataset = scene_dataset.map(load_and_preprocess_image)

    scene_dataset = scene_dataset.shuffle(
        tf.shape(image_samples_path, out_type=tf.int64)[0]
    ).batch(
        BATCH_SIZE
    )

    (train_images, train_labels), (_, _) = keras.datasets.mnist.load_data()
    train_images = train_images.reshape(train_images.shape[0], 28, 28, 1).astype('float32')
    train_images = (train_images - 127.5) / 127.5
    train_dataset = tf.data.Dataset.from_tensor_slices(train_images).shuffle(BUFFER_SIZE).batch(BATCH_SIZE)

    return scene_dataset, train_dataset


def load_and_preprocess_image(path):
    image = tf.io.read_file(path)
    return preprocess_image(image)


def preprocess_image(image):
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [224, 224])
    image = (image - 127.5) / 127.5  # [-1, 1] TODO: Also try [0, 1]

    return image
