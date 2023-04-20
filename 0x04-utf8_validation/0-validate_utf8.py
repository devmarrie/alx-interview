#!/usr/bin/python3
"""
UTF-8 Validation
determines if a given data set represents
a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Args:
        data
    Return:
          True if valid else False
    """
    rem_byte = 0
    for i in data:
        if rem_byte == 0:
            if i >> 5 == 0b110:
                rem_byte = 1
            elif i >> 4 == 0b1110:
                rem_byte = 2
            elif i >> 3 == 0b11110:
                rem_byte = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if rem_byte >> 6 != 0b01:
                return False
            rem_byte -= 1
        return rem_byte == 0
