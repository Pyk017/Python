"""
Given a list of digits. The task is to find out the number of possible decoding of the given digit sequence.

Assume that the input list contains valid digits from 0 to 9 and there are no leading 0's, no trailing 0's and no two or
 more consecutive 0's in the input list.

Let 1 represent 'A', 2 represent 'B', …, 26 represent 'Z'.

Write a python function which accepts the list of digits and returns the total number of decoding possible from given
digit sequence.

Sample Input	          Expected Output	                            Remark
digit_list=[1 ,2 ,2 ,4]	        5	            The possible decoding are "ABBD", "LBD", "AVD", "ABX","LX"
digit_list=[1 ,2 ,2]	        3	                The possible decoding are "ABB", "LB", "AV".
"""
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def recur(digits, i, n, string, res):
    if i == n:
        res.append(string)

    temp = 0
    for j in range(i, min(i+1, n-1) + 1):
        temp = (temp * 10) + digits[j]
        if temp <= 26:
            recur(digits, j+1, n, string + alpha[temp - 1], res)


digit = [1, 2, 2]
result = []
strings = ''
recur(digit, 0, len(digit), strings, result)
print(len(result))
