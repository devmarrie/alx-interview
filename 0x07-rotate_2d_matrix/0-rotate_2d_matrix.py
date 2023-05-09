#!/usr/bin/python3
"""
rotate it 90 degrees clockwise
given a matrix
"""


def rotate_2d_matrix(matrix):
    """
    Takes in a 2D matrix
    Returns nothing
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
