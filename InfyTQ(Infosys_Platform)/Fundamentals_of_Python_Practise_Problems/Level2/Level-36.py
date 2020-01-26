"""
Part-1:
Write a python function which accepts a string of words and a target word, and returns the list of the positions of the
target word in the string of words.

Sample input
input String- we dont need no education we dont need no thought control no we dont
target word- dont

Expected output
[1, 6, 13 ]

Part-2:
Write a python function which accepts a string of words and returns a dict which contains the words in the input string
as key and the list of positions of these words in the input string as value. Use the function written in part-1.

Sample input
we dont need no education we dont need no thought control no we dont

Expected Output
{'no': [3, 8, 11], 'thought': [9], 'dont': [1, 6, 13], 'need': [2, 7], 'control': [10], 'we': [0, 5, 12],
'education': [4]}

Note:
1.The words are separated by a single space.
2.There are no punctuation marks or upper case letters.
"""


def find_target_positions(input_string, target_word):
    target_list = []
    i = 0
    input_string = input_string.split()
    while target_word in input_string:
        target_list.append(input_string.index(target_word) + i)
        input_string.remove(target_word)
        i += 1

    return target_list


def find_inverted_index(inp_string):
    target_dict = {}
    new_string = set(inp_string.split())
    for i in new_string:
        target_dict[i] = find_target_positions(inp_string, i)

    return target_dict


string = "we dont need no education we dont need no thought control no we dont"
result_dict = find_inverted_index(string)
print(result_dict)
