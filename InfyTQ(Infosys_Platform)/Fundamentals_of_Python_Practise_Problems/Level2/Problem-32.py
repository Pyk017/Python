"""
Given an integer n, write a Python function to return True, if it possible to represent it as a sum of the squares of
two different integers, else return False.
"""
import math as m


def check_squares(number):
    for i in range(m.ceil(m.sqrt(number))):
        a = m.sqrt(number - i*i)
        if a.is_integer():
            return True

    return False


num = 68
print(check_squares(num))
