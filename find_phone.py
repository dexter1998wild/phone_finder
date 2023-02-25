import processor
import sys

try:
    image = sys.argv[1]
except:
    raise Exception('No file found')
    
test_out = processor.phone_finder(image)
print(str(test_out[0]) + ' ' + str(test_out[1]) )