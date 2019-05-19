###########################
# ### General constants ###
###########################

# Shape of the dataset and generator output images.
IMG_SHAPE = (224, 224)

# Number of channels of the dataset and generator output images.
N_CHANNELS = 3

# Dataset batch size
BATCH_SIZE = 256

# Debug logging
DEBUG_LOG = False

###################################
# ### Dataset related constants ###
###################################

# How many classes will be used for training.
MAX_CLASSES = 1

# How many samples should be used from each class.
MAX_SAMPLES_PER_CLASS = 100

#################################
# ### Model related constants ###
#################################

# Noise size for the input of the Generator model.
GEN_NOISE_INPUT_SHAPE = 100

# Defines an interval for saving checkpoints based on epochs.
CKPT_SAVE_INTERVAL = 15

# Defines an interval for saving generator image samples based on epochs.
GEN_SAMPLE_SAVE_INTERVAL = 10
