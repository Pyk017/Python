"""
Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.
It should return a list in which the first value should be letter count and second value should be digit count.
Ignore the spaces or any other special character in the sentence.

Sample Input	    Expected Output
Infosys 123	            [7,3]
ABCEFG	                [6,0]
"""
import string


def count_digits_letters(sent):
    ls = [0, 0]
    for i in sent:
        if i in string.ascii_letters:
            ls[0] += 1
        elif i in string.digits:
            ls[1] += 1

    return ls


sentence = "Infosys Mysore 570027"
print(count_digits_letters(sentence))
