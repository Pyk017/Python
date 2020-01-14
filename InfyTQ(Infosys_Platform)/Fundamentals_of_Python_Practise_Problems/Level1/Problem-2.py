"""
Write a python function which accepts a string containing a pattern of brackets and return True if the pattern of
brackets is correct. Otherwise it returns False. The string of brackets is corrects if it satisfies the following
conditions:
1. Number of opening and closing brackets are equal.
2. Pattern should not start with closing bracket and end with opening bracket.

Sample Input :
)()((()())
()((())())

Sample Output :
False
True
"""


def bracket_pattern(input_str):
    if input_str.count('(') == input_str.count(')') and not input_str.startswith(')') and not input_str.endswith('('):
        return True
    return False


input_string = '(())()'
print(bracket_pattern(input_string))
