### Indoor Scene Recognition

[Indoor scene recognition](http://web.mit.edu/torralba/www/indoor.html) is a challenging open problem in high level vision. Most scene recognition models that work well for outdoor scenes perform poorly in the indoor domain. The main difficulty is that while some indoor scenes (e.g. corridors) can be well characterized by global spatial properties, others (e.g., bookstores) are better characterized by the objects they contain. More generally, to address the indoor scenes recognition problem we need a model that can exploit local and global discriminative information.

### Database
The [database](http://groups.csail.mit.edu/vision/LabelMe/NewImages/indoorCVPR_09.tar) contains 67 Indoor categories, and a total of 15620 images. The number of images varies across categories, but there are at least 100 images per category. All images are in jpg format. The images provided here are for research purposes only.

### Evaluation
For the results in the paper we use a subset of the dataset that has the same number of training and testing samples per class. The partition that we use is:

- [TrainImages.txt](http://web.mit.edu/torralba/www/TrainImages.txt): contains the file names of each training image. Total 67*80 images.
- [TestImages.txt](http://web.mit.edu/torralba/www/TestImages.txt): contains the file names of each test image. Total 67*20 images.

### Annotations
A subset of the images are segmented and annotated with the objects that they contain. The [annotations](http://groups.csail.mit.edu/vision/LabelMe/NewImages/indoorCVPR_09annotations.tar) are in LabelMe format.

### Paper
A. Quattoni, and A.Torralba. [Recognizing Indoor Scenes](http://people.csail.mit.edu/torralba/publications/indoor.pdf). IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2009.
