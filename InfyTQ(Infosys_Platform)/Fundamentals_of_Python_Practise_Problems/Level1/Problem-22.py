"""
Write a python function to print the given number of diagonal lines of stars.

Sample input: 5

Expected output:
*
.*
..*
...*
....*

Note: Setting the end parameter of the print function to empty string prevents the issuing of the new line.
Example: print(".",end="") will maintain the cursor in the same line after
"""


def diagonal_stars(number):
    for i in range(1, number+1):
        for j in range(1, i):
            print('.', end='')
        print('*')


num = 6
diagonal_stars(num)
