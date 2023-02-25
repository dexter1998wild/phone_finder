import sys
import math
import processor


  

def main():
                            
    try:
        file_path = sys.argv[1]                             # Reads the file path
        label_path = file_path + '/labels.txt'              # Gets the path to the labels file
    except:
        raise Exception("Invalid file path")

    
    found_counter = size_counter = 0
    with open(label_path) as fp:
        
      for line in fp:
        line = line.rstrip('\n')
        split = line.split(' ')
        im = file_path+'/'+split[0]                         # Path to individual image
                        
        res = [float(split[1]), float(split[2])]            # Label for image      
        
        
        size_counter = size_counter+1
        test = processor.phone_finder(im)                   # processes individual image to get coordinates
       
        if (math.pow((res[0]-test[0]),2) + math.pow((res[1]-test[1]),2) <= math.pow(0.05,2)):   #Check to see if output conforms to required spec
            found_counter = found_counter + 1

            
              
        
    accuracy = round((found_counter / size_counter) * 100 , 3)
    print("Model gives " + str(accuracy) + "% accurate result of the prediction")
        
if __name__=='__main__':
    main()
