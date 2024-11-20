#!/usr/bin/python3
"""
THis is to Rotate 2-D matrix
"""


def rotate_2d_matrix(matrix):
    """
    this module rotate two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    n = len(matrix)
    for i in range(int(n / 2)):
        k = (n - i - 1)
        for j in range(i, k):
            m = (n - 1 - j)
            # the actual number
            tmp = matrix[i][j]
            # changing the top for left
            matrix[i][j] = matrix[m][i]
            # changing left for bottom
            matrix[m][i] = matrix[k][m]
            # changing bottom for right
            matrix[k][m] = matrix[j][k]
            # changing right for top
            matrix[j][k] = tmp
