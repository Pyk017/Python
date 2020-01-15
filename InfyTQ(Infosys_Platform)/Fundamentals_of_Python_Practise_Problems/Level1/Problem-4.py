"""
Given a list of numbers, write a python function which returns true if one of the first 4 elements in the list is 9.
Otherwise it should return false.
The length of the list can be less than 4 also.

Sample Input	    Expected Output
[1, 2, 9, 3, 4]	        True
[1, 2, 9]	            True
[1, 2, 3, 4]	        False
"""


def find_nine(nums):
    return True if 9 in nums[:4] else False


num = [1, 9, 3, 4]
print(find_nine(num))
