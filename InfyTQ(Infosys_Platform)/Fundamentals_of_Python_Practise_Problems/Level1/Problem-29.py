"""
Given a list of numbers, write a python function to exchange the first n/2 elements of a list with the last n/2 elements
The function should return the new list.
n represents the number of elements in the list. Assume that it will always be even.

Sample Input	                Expected Output
[1,2,3,4,5,6,7,8,9,10]	    [10,9,8,7,6,1,2,3,4,5]
"""


def exchange_list(number_list):
    n = len(number_list)
    # back_list = number_list[n//2:][::-1]
    # print(back_list, number_list[:n//2])
    return number_list[n//2:][::-1] + number_list[:n//2]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(exchange_list(numbers))
