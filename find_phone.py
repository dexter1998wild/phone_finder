'''
Find Phone
'''

import sys
import processor

try:
    image = sys.argv[1] #RENAME HERE
except Exception as exc:
    raise FileNotFoundError('No file found') from exc


test_out = processor.phone_finder(image)
print(str(test_out[0]) + ' ' + str(test_out[1]) )
