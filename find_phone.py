
'''
Find Phone
'''

import sys
import processor

try:
    test_image = sys.argv[1]
except Exception as exc:
    raise FileNotFoundError('No file found') from exc


test_out = processor.phone_finder(test_image)
print(str(test_out[0]) + ' ' + str(test_out[1]) )