"""
The D33P language includes three types of tokens: open parentheses, close parentheses, and integers.
An expression is well-formed if it contains balanced parentheses, and each integer correctly indicates its depth:
the number of nested sets of parentheses that surround that integer.
Implement correct depth, which takes a list of tokens as input and returns True if and only if a prefix of the input is
a well-formed D33P expression.

Assume that the input contains a balanced set of nested parentheses with single-digit positive integers surrounded by
parentheses.
You only need to check that the integers indicate the correct depths.

Sample Input	        Expected Output
list('(1)')	                True
list('(2)')	                False
list('((2)((3)))')	        True
list('((3)(2))')	        False
"""


def check_correct_depth(input_list):
    for i in input_list:
        if i != '(' and i != ')':
            starting = input_list.split(i)[0].count('(')
            ending = input_list.split(i)[1].count(')')
            if starting < int(i) or ending < int(i):
                return False

    return True


input_lists = ['(1)', '(2)', '((2)((3)))', '((2)(3))', '((3)(2))', '(((3)((4))(3))(2)((3)))']
for k in input_lists:
    print(k, check_correct_depth(k))
