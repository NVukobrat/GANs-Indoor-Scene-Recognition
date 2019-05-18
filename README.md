### Summary
Apply Generative Adversarial Network (GAN) to generate indoor scene images. 

This model could be used to generate new indoor scene images and by that extend an available dataset of indoor scenes. Newly generated images should improve accuracy of indoor scene classifier model.

### Cases
##### Single class with single image
Training process of the Generator model is apply to the single class containing single image generator results converge to recognizable images really fast. This results in high over-fit. In case of Generator model, for any input noise tensor, output will be the same image used in the training process.

```bash
Number of epochs: 10.000
Training duration: 1h 45m 9s
```
<center>
<table style="width: 100%;">
    <tr>
        <td>Original Image</td>
    </tr>
    <tr>
        <td><img src="assets/images/single_class_single_image/joyeria_rometsch03.jpg" alt=""></td>
    </tr>
</table>
</center>

<center>
<table style="width: 100%;">
    <tr>
        <td>Epoch 10</td>
        <td>Epoch 300</td>
        <td>Epoch 500</td>
    </tr>
    <tr>
        <td><img src="assets/images/single_class_single_image/epoch_examples/image_at_epoch_0010_0000.png" alt=""></td>
        <td><img src="assets/images/single_class_single_image/epoch_examples/image_at_epoch_0300_0000.png" alt=""></td>
        <td><img src="assets/images/single_class_single_image/epoch_examples/image_at_epoch_0500_0000.png" alt=""></td>
    </tr>
    <tr>
        <td>Epoch 700</td>
        <td>Epoch 900</td>
        <td>Epoch 1500</td>
    </tr>
    <tr>
        <td><img src="assets/images/single_class_single_image/epoch_examples/image_at_epoch_0700_0000.png" alt=""></td>
        <td><img src="assets/images/single_class_single_image/epoch_examples/image_at_epoch_0900_0000.png" alt=""></td>
        <td><img src="assets/images/single_class_single_image/epoch_examples/image_at_epoch_1500_0000.png" alt=""></td>
    </tr>
    <tr>
        <td>Epoch 3.000</td>
        <td>Epoch 5.000</td>
        <td>Epoch 10.000</td>
    </tr>
    <tr>
        <td><img src="assets/images/single_class_single_image/epoch_examples/image_at_epoch_3000_0000.png" alt=""></td>
        <td><img src="assets/images/single_class_single_image/epoch_examples/image_at_epoch_5000_0000.png" alt=""></td>
        <td><img src="assets/images/single_class_single_image/epoch_examples/image_at_epoch_10000_0000.png" alt=""></td>
    </tr>
</table>
</center>

<center>
<table style="width: 100%;">
    <tr>
        <td>Generator Loss</td>
        <td>Discriminator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/single_class_single_image/loss_examples/Screenshot from 2019-05-18 14-44-03.png"
                 alt=""></td>
        <td><img
                src="assets/images/single_class_single_image/loss_examples/Screenshot%20from%202019-05-18%2014-44-16.png"
                alt=""></td>
    </tr>
</table>
</center>

### TODO:
- Repeat single class with 1 image to get proper loss results.
- Try single class with 3 images.
- Try single class with 10 images.
- Try single class with 100 images.
- Try full single class.
- Try 3 classes with 1 image.
- Try 3 classes with 100 images.
- Try full 3 classes.
- Try full dataset with 100 samples per class.
- Try full dataset.

### Notes
- [Cool list of available datasets](https://github.com/awesomedata/awesome-public-datasets)