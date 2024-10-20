# udacity_python_assignment

# Image Classification for a City Dog Show
## Project Goal
Improving your programming skills using Python.
In this project, you will use a created image classifier to identify dog breeds. We ask you to focus on Python and not on the actual classifier.

## Description:
Your city is hosting a citywide dog show and you have volunteered to help the organizing committee with contestant registration. Every participant that registers must submit an image of their dog along with biographical information about their dog. The registration system tags the images based upon the biographical information.

Some people are planning on registering pets that aren’t actual dogs.

You need to use an already developed Python classifier to make sure the participants are dogs.

Note, you DO NOT need to create the classifier. It will be provided to you. You will need to apply the Python tools you just learned to USE the classifier.

## Important Notes:
For this image classification task, you will be using an image classification application using a deep learning model called a convolutional neural network (often abbreviated as CNN). CNNs work particularly well for detecting features in images like colors, textures, and edges; then using these features to identify objects in the images. You'll use a CNN that has already learned the features from a giant dataset of 1.2 million images called ImageNet(opens in a new tab). There are different types of CNNs that have different structures (architectures) that work better or worse depending on your criteria. With this project, you'll explore the three different architectures (AlexNet, VGG, and ResNet) and determine which is best for your application.

We have provided you with a classifier function in classifier.py that will allow you to use these CNNs to classify your images. The test_classifier.py file contains an example program that demonstrates how to use the classifier function. For this project, you will be focusing on using your Python skills to complete these tasks using the classifier function.

Remember that certain breeds of dogs look very similar. The more images of two similar-looking dog breeds that the algorithm has learned from, the more likely the algorithm will be able to distinguish between those two breeds. We have found the following breeds to look very similar: Great Pyrenees(opens in a new tab) and Kuvasz(opens in a new tab), German Shepherd(opens in a new tab) and Malinois(opens in a new tab), Beagle(opens in a new tab) and Walker Hound(opens in a new tab), amongst others.

## Command line:
`python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt`

`python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt`

`python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt`

# Result Comparision based on using different models
| Total Images | Dog Images | Not-a-Dog Images |
|--------------|------------|-------------------|
| 40           | 30         | 10                |

| CNN       | % Not-a-Dog Correct | % Dogs Correct | % Breeds Correct | % Match Labels |
|-----------|----------------------|----------------|------------------|-----------------|
| RestNet   |   90.00              |      100.00    |    90.00         |    82.50        |
| AlexNet   |    100.00            |     100.00     |    80.00         |     75.00       |
| VGG       |    100.00            |     100.00     |     93.33        |     87.50     |
		
## Questions regarding Uploaded Image Classification:

1. Did the three model architectures classify the breed of dog in Dog_01.jpg to be the same breed? If not, report the differences in the classifications.

    Answer:  YES


2. Did each of the three model architectures classify the breed of dog in Dog_01.jpg to be the same breed of dog as that model architecture classified Dog_02.jpg? If not, report the differences in the classifications.

    Answer: 

    RESNET: 
    Dog_02.jpg classified golden retriever  as  orangutan, orang, orangutang, pongo pygmaeus instead.

    ALEXNET:
    Dog_02.jpg classified golden retriever  as norwich terrier

    VGG:
    Dog_02.jpg  classified correctly as golden retriever. 

3. Did the three model architectures correctly classify Animal_Name_01.jpg and Object_Name_01.jpg to not be dogs? If not, report the misclassifications.

    Answer: 
    For Animal_Name_01.jpg and Object_Name_01.jpg, all 3 model architectures can classify that those are not a dog. 

4. Based upon your answers for questions 1. - 3. above, select the model architecture that you feel did the best at classifying the four uploaded images. Describe why you selected that model architecture as the best on uploaded image classification.

    Answer:
    I select VGG as
    only VGG can classify the dog upside down images correctly, while AlexNet and ResNet model architectures could not classify the upside down image as a dog.
