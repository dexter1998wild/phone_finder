# Phone Finder
This project is designed to find phones in images using image processing techniques. The project consists of two files:

train_phone_finder.py: This file contains the code to train the model to detect phones in the images.

find_phone.py: This file uses the trained model to find the location of the phone in the given image.

## Installation
To use this project, you need to have Python 3 installed on your system. You also need to install the following libraries:
```
OpenCV
Matplotlib
```
You can install these libraries by running the following command:

```
pip install -r requirements.txt
```
### Usage
#### Training the Model
To train the model, you need to run the train_phone_finder.py file. The file takes the following arguments:

```
python train_phone_finder.py <path_to_training_data>
```
data_path: The path to the folder containing the training data.

#### Finding Phone in an Image
To find the phone in an image, you need to run the find_phone.py file. The file takes the following arguments:

```
python find_phone.py <path_to_image>
```
image_path: The path to the image in which you want to find the phone.
The output of the find_phone.py file will be the coordinates of the center of the phone in the image.
