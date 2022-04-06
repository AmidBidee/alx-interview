#!/usr/bin/python3
"""
the pascal's triangle module
algorithm:
    - declare an empty list to hold values.
    - use a for loop to iterate through 0 to n - 1,
        append the sub-lists to the list
    - append 1 to the list.
    - use another for loop to define the value of the number inside
        the triangle adjancent row.
"""


def pascal_triangle(n: int):
    """
    returns a list of lists of integers following the pascal's triangle

    Args:
        n [int]: height of triangle

    Returns:
        triangle [list]: a list of lists of integers
                        following the pascal's triangle
    """
    triangle = []

    for i in range(n):
        triangle.append([1])
        for j in range(1, i):
            triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        if (n > 0):
            if i != 0:
                triangle[i].append(1)
    return triangle
