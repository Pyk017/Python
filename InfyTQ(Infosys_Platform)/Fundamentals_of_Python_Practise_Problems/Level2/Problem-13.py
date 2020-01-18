"""
Write a Python function which accepts three numbers and return True if
a. one of the three numbers is "close" to any one of the numbers (differing from a number by atmost 1), and
b. Number that is left out is "far", differing from both other values by 2 or more.
Return False if the above mentioned conditions are not satisfied.

Input : 4 1 3       Output : True
Input : 5 6 7       Output : False
"""


def close_number(num1, num2, num3):
    s = set()
    count = 0
    for i in [num1, num2, num3]:
        if i in s:
            count += 1

        s.add(i)
        s.add(i - 1)
        s.add(i + 1)

    if count == 1:
        return True
    return False


print(close_number(5, 4, 2))
