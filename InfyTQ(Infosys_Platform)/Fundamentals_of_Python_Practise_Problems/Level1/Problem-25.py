"""
Write a python function that accepts a list of words and returns the list of integers representing the length of the
corresponding words.

Sample Input	        Expected Output
[cat, Come]	                [3,4]
"""


def list_of_count(word_list):
    return list(map(len, word_list))


word = ["COme", "here"]
print(list_of_count(word))
