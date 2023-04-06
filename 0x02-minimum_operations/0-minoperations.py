#!/usr/bin/python3
"""Minimum Operations required to generate H n times
   Operations that can be performed include CopyAll and Paste
"""
import math


def minOperations(n):
    """"Loop over all possible prime factors up to the square root
    """
    if n < 1:
        return 0
    
    operations = 0
    i = 2
    
    while i <= math.sqrt(n):
        if n % i == 0:
            operations += i
            n //= i
        else:
            i += 1
    
    operations += n
    
    return operations

