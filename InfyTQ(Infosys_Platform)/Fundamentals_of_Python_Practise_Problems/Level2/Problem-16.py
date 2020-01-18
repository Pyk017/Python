"""
Write a Python function to rotate the list of elements by N positions. The Function should return the rotated list.

    Sample Input                                                Sample Output
Input list : [1, 2, 3, 4, 5, 6]                               [5, 6, 1, 2, 3, 4]
Number of positions to be rotated = 2

Input list : [1, 2, 3, 4, 5, 6]                               [3, 4, 5, 6, 1, 2]
Number of positions to be rotated = 4
"""


def rotate_list(input_list, n):
    return input_list[-n:] + input_list[:-n]


print(rotate_list([1, 2, 3, 4, 5, 6], 2))
