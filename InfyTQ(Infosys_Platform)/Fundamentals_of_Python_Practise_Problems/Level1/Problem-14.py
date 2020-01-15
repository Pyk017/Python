"""
Write a python function to find and display the five digit number in which the first digit is two more than the second,
the second digit is two more than the third, the fourth digit is two less than the third, and the last digit is two more
than the fourth. The sum of the third, fourth and fifth digit is equals to first digit. The Sum of all digits is 19.
"""


def find_five_digit(num):
    x = 0  # Let x be the first digit, then second digit will be x-2, and third digit will be x-4, according to ques.
    y = 0  # Let y be the fifth digit, and then y-2 will be the fourth digit.
    y = 3  # By the first condition, x-4 + y-2 + y = x  that is The sum of 3rd, 4th, 5th digits equals to 1st.
    x = int((num + 2) / 3)  # By the last condition, x + x-2 + x-4 + 1 + 3 = 19, First Element
    b = x - 2  # Second Element
    c = x - 4  # Third Element
    y = 3  # Fifth Element
    z = y - 2  # Fourth Element
    return str(x) + str(b) + str(c) + str(z) + str(y)


number = 19
print(find_five_digit(number))
