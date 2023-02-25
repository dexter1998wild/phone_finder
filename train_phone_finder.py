import cv2
from matplotlib import image as mpimg
import sys
import math
import processor


def main():
    """_summary_

    Raises:
        Exception: _description_
    """
    try:
        # Reads the file path
        file_path = sys.argv[1]
        # Gets the path to the labels file
        label_path = file_path + '/labels.txt'
    except Exception as exc:
        raise FileNotFoundError("Invalid file path") from exc

    found_counter = size_counter = 0
    with open(label_path) as fp:
        sents = fp.readlines() #RENAME HERE

    for line in sents:
        line = line.rstrip('\n')
        split = line.split(' ')
        # Path to individual image
        im = file_path+'/'+split[0] #RENAME HERE

        # Label for image
        res = [float(split[1]), float(split[2])] #RENAME HERE

        size_counter = size_counter+1
        # processes individual image to get coordinates
        test = processor.phone_finder(im)

        # Check to see if output conforms to required spec
        if math.pow((res[0]-test[0]), 2) + math.pow((res[1]-test[1]), 2) <= math.pow(0.05, 2):
            found_counter = found_counter + 1

    accuracy = round((found_counter / size_counter) * 100, 3)
    print("Model gives " + str(accuracy) +
          "% accurate result of the prediction")


if __name__ == '__main__':
    main()
