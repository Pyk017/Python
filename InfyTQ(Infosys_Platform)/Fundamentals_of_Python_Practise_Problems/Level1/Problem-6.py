"""
Write a python function which accepts a list of numbers and returns true, if 1, 2, 3 appears in sequence in the list.
Otherwise, it should return false.

Sample Input	    Expected Output
[1, 1, 2, 3, 1]	        True
[1, 1, 2, 4, 3]	        False
"""


def list123(nums):
    return True if '123' in ''.join(list(map(str, nums))) else False


num = [1, 2, 3, 4, 5]
print(list123(num))
