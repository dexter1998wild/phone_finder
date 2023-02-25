'''
Processor
'''

import cv2 as cv
from matplotlib import image as mpimg


def phone_finder(im):
    """_summary_

    Args:
        im (_type_): _description_

    Returns:
        _type_: _description_
    """
    image = mpimg.imread(im)
    h, w = image.shape[0], image.shape[1] #RENAME HERE
    # Converts RGB ro Grey
    grey = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

    # Filter the phone from background
    _, threshold = cv.threshold(grey, 65, 255, cv.THRESH_BINARY)
    dilated_image = cv.dilate(
        cv.dilate(cv.dilate(threshold, None), None), None)   # Fill some holes

    # Revert effects of dilation on shape
    eroded_image = cv.erode(
        cv.erode(cv.erode(dilated_image, None), None), None)

    # Find shape (object detection)
    contours, _ = cv.findContours(
        eroded_image, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    rc = cv.minAreaRect(contours[0]) #RENAME HERE
    centre = [rc[0][0]/w, rc[0][1]/h]

    return [round(centre[0], 4), round(centre[1], 4)]
