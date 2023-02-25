<<<<<<< Updated upstream
import processor
=======
'''
Find Phone
'''

>>>>>>> Stashed changes
import sys
import processor

try:
<<<<<<< Updated upstream
    image = sys.argv[1]
except:
    raise Exception('No file found')
    
test_out = processor.phone_finder(image)
print(str(test_out[0]) + ' ' + str(test_out[1]) )

=======
    image = sys.argv[1] #RENAME HERE
except Exception as exc:
    raise FileNotFoundError('No file found') from exc


test_out = processor.phone_finder(image)
print(str(test_out[0]) + ' ' + str(test_out[1]) )
>>>>>>> Stashed changes
