import os
import random
import time

import tensorflow as tf

# Training parameters
BATCH_SIZE = 32
MAX_SAMPLES_PER_CLASS = 3

# Dataset images parameters
IMG_SHAPE = (224, 224)
NUM_CHANNEL = 3


def load_normalized_dataset(path):
    """
    Loads dataset,  normalizes it to [-1, +1] values,
    and shuffles.

    Arguments:
        path: The relative path to the dataset.

    Returns:
        The normalized dataset.
    """
    start = time.time()

    image_samples_path = list()
    for class_dir in os.listdir(path):
        counter = 0
        full_class_dir = os.path.join(path, class_dir)
        for image_name in os.listdir(full_class_dir):
            counter += 1

            full_image_name = os.path.join(full_class_dir, image_name)
            image_samples_path.append(full_image_name)

            if counter == MAX_SAMPLES_PER_CLASS:
                break

    random.shuffle(image_samples_path)

    scene_dataset = tf.data.Dataset.from_tensor_slices(
        image_samples_path
    )

    scene_dataset = scene_dataset.map(load_and_preprocess_image)

    scene_dataset = scene_dataset.batch(
        BATCH_SIZE
    )

    end = time.time()
    print("Execution time: {:.9f}s (load_normalized_dataset)".format(end - start))

    return scene_dataset


def load_and_preprocess_image(path):
    image = tf.io.read_file(path)
    return preprocess_image(image)


def preprocess_image(image):
    image = tf.cond(
        tf.image.is_jpeg(image),
        lambda: tf.image.decode_jpeg(image, channels=NUM_CHANNEL),
        lambda: tf.image.decode_png(image, channels=NUM_CHANNEL))
    image = tf.image.resize(image, IMG_SHAPE)
    image = (image - 127.5) / 127.5  # [-1, 1] TODO: Also try [0, 1]

    return image
