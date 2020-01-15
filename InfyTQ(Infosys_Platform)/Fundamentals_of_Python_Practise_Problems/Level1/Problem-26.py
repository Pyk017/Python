"""
Given a string, write a python function to return True if the strings "mat" and "jet" appear the same number of times
in the given string, else return False.

Note: Perform case insensitive string comparison wherever necessary.

Sample Input	                            Expected Output
Jet on the Mat but mat is too long	            False
mat jet Jet Mat                                 True
"""


def check_occurrence(string):
    string = string.lower()
    return True if string.count('mat') == string.count('jet') else False


input_string = 'Jet on the mat but Mat is too long'
print(check_occurrence(input_string))
