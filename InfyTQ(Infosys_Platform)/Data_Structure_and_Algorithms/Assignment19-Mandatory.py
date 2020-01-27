"""
Given list of numbers sorted in ascending order. Write a python function which searches for a given number in the list.
The given number may occur more than once in the list. The function should return the index position at which the last
occurrence of the given element is found. If the number is not found, return -1.
"""


def last_instance(num, st, ed, k):
    return len(num[st: ed + 1]) - 1 - num[st: ed + 1][::-1].index(k)


num_list = [1, 1, 2, 2, 3, 4, 5, 5, 5, 5]
start = 0
end = len(num_list) - 1
key = 5
resultant = last_instance(num_list, start, end, key)
if resultant != -1:
    print("The index position of the last occurrence of the number:", resultant)
else:
    print("Number not found")
