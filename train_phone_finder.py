import sys
import processor


def main():
    """Processes all images in a folder and detects a phone in each image.
    
    Raises:
    - FileNotFoundError: If the folder path is invalid or does not exist.
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
        data = fp.readlines()

    for line in data:
        line = line.rstrip('\n')
        split = line.split(' ')
        # Path to individual image
        img_path = file_path+'/'+split[0] 

        # Label for image
        img_label = [float(split[1]), float(split[2])]

        size_counter = size_counter+1
        # processes individual image to get coordinates
        test = processor.phone_finder(img_path)

        # Check to see if output conforms to required spec
        if ((float(img_label[0])-0.05 <=float(test[0])<= float(img_label[0])+0.05) or (float(img_label[1]) -0.05 <=float(test[1])<= float(img_label[1])+0.05) or (float(img_label[0])-0.05 <=float(test[1])<= float(img_label[0])+0.05) or (float(img_label[1]) -0.05 <=float(test[0])<= float(img_label[1])+0.05) ):
            found_counter = found_counter + 1

    accuracy = round((found_counter / size_counter) * 100, 3)
    print("Model gives " + str(accuracy) +
          "% accurate result of the prediction")


if __name__ == '__main__':
    main()