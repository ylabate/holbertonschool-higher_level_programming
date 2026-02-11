#!/usr/bin/python3
"""Module that returns a list of lists of integers representing Pascal's."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists of integers representing the Pascal’s triangle.
    """
    if n <= 0:
        return []
    triangle = []
    for layer in range(1, n + 1):
        row = []
        for i in range(layer):
            if i == layer - 1 or i == 0:
                row.append(1)
            else:
                row.append(triangle[layer - 2][i - 1] + triangle[layer - 2][i])
        triangle.append(row)
    return triangle
