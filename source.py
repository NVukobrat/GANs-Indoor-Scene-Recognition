from api import dataset
from api import model

# Root path to the dataset
DATASET_PATH = "dataset"

# Last epoch during previous training (in case training
# has continued from the checkpoint).
LAST_EPOCH = 22200

# How many epochs should train last.
EPOCHS = 50000


# TODO: Error — Resource exhausted — optimize training pipeline.
def main():
    # Load dataset
    scene_dataset = dataset.load_normalized_dataset(DATASET_PATH)

    # Create models
    gen_model = model.generator()
    gen_optimizer = model.generator_optimizer()
    dis_model = model.discriminator()
    dis_optimizer = model.discriminator_optimizer()

    # Define model checkpoint
    checkpoint, checkpoint_prefix = model.define_checkpoint(gen_model, gen_optimizer, dis_model, dis_optimizer)

    # Initialize training pipeline.
    model.train(
        real_image_dataset=scene_dataset,
        last_epoch=LAST_EPOCH,
        epochs=EPOCHS,
        gen_model=gen_model,
        gen_optimizer=gen_optimizer,
        dis_model=dis_model,
        dis_optimizer=dis_optimizer,
        checkpoint=checkpoint,
        checkpoint_prefix=checkpoint_prefix,
    )

    return 0


if __name__ == '__main__':
    main()
