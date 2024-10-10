#!/usr/bin/python3
"""Script that calculate pascal triangle of any given number n"""


def pascal_triangle(n):
    """
    function that return the number of the triangle
    """
    triangle = []

    # return empty triangle (trianlgle if n <= 0)
    if n <= 0:
        return triangle
    for i in range(n):
        tri_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                tri_list.append(1)
            else:
                tri_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(tri_list)
    # print the pascal triangle
    return triangle
