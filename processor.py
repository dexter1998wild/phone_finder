'''
Processor
'''

import cv2 as cv
from matplotlib import image as mpimg

def phone_finder(image_path):
    """Process image to detect phone and return center coordinates.

    Args:
      image_path (str): The path of the input image to be processed.

    Returns:
      list: A list containing the x and y coordinates of the center of the detected phone.

    """
    image = mpimg.imread(image_path)
    height, width = image.shape[0], image.shape[1] 
    # Converts RGB ro Grey
    grey = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

    # Filter the phone from background
    _, threshold = cv.threshold(grey, 65, 255, cv.THRESH_BINARY)

    # Fill some holes
    dilated_image = cv.dilate(
        cv.dilate(cv.dilate(threshold, None), None), None)   

    # Revert effects of dilation on shape
    eroded_image = cv.erode(
        cv.erode(cv.erode(dilated_image, None), None), None)

    # Find shape (object detection)
    contours, _ = cv.findContours(
        eroded_image, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    rectangle = cv.minAreaRect(contours[0])
    centre = [rectangle[0][0]/width, rectangle[0][1]/height]

    return [round(centre[0], 4), round(centre[1], 4)]
