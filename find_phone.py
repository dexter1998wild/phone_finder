<<<<<<< HEAD
import processor
import sys

try:
    image = sys.argv[1]
except:
    raise Exception('No file found')
    
test_out = processor.phone_finder(image)
=======
import processor
import sys

try:
    image = sys.argv[1]
except:
    raise Exception('No file found')
    
test_out = processor.phone_finder(image)
>>>>>>> 098a205324abb03f42190b81439820c9e857f4df
print(str(test_out[0]) + ' ' + str(test_out[1]) )