"""
Write a python function to add 'ing' at the end of a given string and return the new string. If the given string already
ends with 'ing' then add 'ly'. If the length of the given string is less than 3, leave it unchanged.

Sample Input :
sleep
amazing
is

Sample Output :
sleeping
amazingly
is
"""


def add_string(str1):
    if len(str1) < 3:
        return str1
    if str1.endswith('ing'):
        return str1 + 'ly'
    return str1 + 'ing'


string = "com"
print(add_string(string))
