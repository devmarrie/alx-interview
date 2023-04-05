#!/usr/bin/python3
"""Minimum Operations required to generate H n times
   Operations that can be performed include CopyAll and Paste
"""
def minOperations(n):
    """Returns an integer of the number of times we can copy and paste H
    If n is impossible to achieve, return 0
    """
    if n <= 1:
        return 0
    # start with one
    h_count = 1
    times = 0
    while n > 1:
        if n % h_count == 0:
            times += 2
            h_count += 1
            n = n - h_count
        else:
            times += 1
            h_count += h_count
        n -= h_count
    return times
