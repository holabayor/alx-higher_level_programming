#!/usr/bin/python3
"""Read file module
"""


def pascal_triangle(n):
    """
    This function prints the pascal triangle of n
    """
    pascal = [[0]*i for i in range(1, n+1)]
    for i in range(n):
        pascal[i][0] = 1
        pascal[i][-1] = 1
        for j in range(i//2):
            pascal[i][j+1] = pascal[i-1][j] + pascal[i-1][j+1]
            pascal[i][i-j-1] = pascal[i-1][j] + pascal[i-1][j+1]

    return pascal
