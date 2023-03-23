#!/usr/bin/python3
"""
The pascal triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []
    else:
        # create the first row
        triangle = [[1]]

        # loop through the other rows
        for i in range(1, n):
            row = [1]
            # loop through the previous row to find current
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle
