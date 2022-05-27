#!/usr/bin/python3
"""0-rotate_2d_matrix.py module
"""


def rotate_2d_matrix(matrix):
    """rotates an n x n 2D matrix
    90 degrees clockwise
    """
    matrix.reverse()

    n = len(matrix)
    for i in range(0, n):
        for j in range(i + 1, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
