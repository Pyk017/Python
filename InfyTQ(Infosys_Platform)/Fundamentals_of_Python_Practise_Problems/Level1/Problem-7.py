"""
Given two numbers, write a python function which returns true if first number is a seed of second number.
Otherwise it returns false.
A number X is said to be a seed of number Y, if multiplying X by its each digit equates to Y

For example, 123 is a seed of 738 as 123*1*2*3 = 738.


Sample Input	Expected Output
123,738	            True
45,1000	            False
"""


def seed_no(num, ref):
    num_str = str(num)
    temp = num
    for i in num_str:
        temp *= int(i)

    return True if temp == ref else False


number = 45
ref_no = 1000
print(seed_no(number, ref_no))
