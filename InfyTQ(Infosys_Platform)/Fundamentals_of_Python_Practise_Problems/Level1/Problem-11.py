"""
Write a python function which accepts a sentence and returns a list in which first value is the count of upper case
letters and second value is the count of lower case letters in the sentence.
Ignore spaces, numbers and other special characters if any.

Sample Input	        Expected Output
Hello world!	            [1, 9]
Welcome to Mysore	        [2, 13]
"""
import string


def find_upper_and_lower(sentence):
    ls = [0, 0]
    for i in sentence:
        if i in string.ascii_uppercase:
            ls[0] += 1
        elif i in string.ascii_lowercase:
            ls[1] += 1

    return ls


sent = "Come Here"
print(find_upper_and_lower(sent))
