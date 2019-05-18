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

<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        table {
            width: 100%
        }
    </style>
</head>
<body>
<table>
    <tr>
        <th>Original Image</th>
    </tr>
    <tr>
        <td><img src="assets/images/single_class_single_image/joyeria_rometsch03.jpg" alt="" ></td>
    </tr>
</table>
</body>
</html>

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