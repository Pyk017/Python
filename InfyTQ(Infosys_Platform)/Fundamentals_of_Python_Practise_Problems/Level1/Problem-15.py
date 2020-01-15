"""
Write a python function which accepts a list of numbers and returns true if the list contains a 2 next to a 2.
Otherwise it should return false.

Sample Input	        Expected Output
[ 1,2,1,2,3,4,5,2,2]	    True
[3,2,5,1,2,1,2]	            False
"""


def check_22(num_list):
    return True if '22' in ''.join(list(map(str, num_list))) else False


print(check_22([3, 2, 5, 1, 2, 1, 2, 5, 2]))
