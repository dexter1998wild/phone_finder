import cv2 as cv
from matplotlib import image as mpimg
import sys
import math

def phone_finder(im):
  image = mpimg.imread(im)
  h,w = image.shape[0],image.shape[1]
  grey = cv.cvtColor(image, cv.COLOR_RGB2GRAY)                          # Converts RGB ro Grey
        
  _,threshold = cv.threshold(grey,65,255,cv.THRESH_BINARY)                      # Filter the phone from background
  dilated_image = cv.dilate(cv.dilate(cv.dilate(threshold, None), None), None)   # Fill some holes
        
  eroded_image = cv.erode(cv.erode(cv.erode(dilated_image, None), None), None)      # Revert effects of dilation on shape
        
  contours, _ = cv.findContours(eroded_image, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # Find shape (object detection)
  
      
  rc = cv.minAreaRect(contours[0])              
  centre = [rc[0][0]/w, rc[0][1]/h]
        
  return [round(centre[0],4) ,round(centre[1] ,4)]
