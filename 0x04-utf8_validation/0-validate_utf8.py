#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
param data:
          A list of integers representing 1 byte of data each
return:
        True if data is a valid UTF-8 encoding, else False
"""


def validUTF8(data):
    """
    How many bytes are remaining
    rem_byte == 0 means we are on the first character
    Args:
        data
    Return:
          True if valid else False
    """
    rem_byte = 0
    for i in data:
        if i >= 256:
            return False
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
            if i >> 6 != 0b10:
                return False
            rem_byte -= 1
    return rem_byte == 0
