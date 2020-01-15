"""
Given two positive integers. Write a python function to return the greatest common divisor of the given numbers.

Sample Input	    Expected Output
14 and 35	            7
800 and 2800	      400
"""


def find_gcd(num1, num2):
    while num2 != 0:
        num2, num1 = num1 % num2, num2

    return num1


number1 = 14
number2 = 35
print(find_gcd(number1, number2))
