"""
Given a list of lists of integers, write a python function, index_of_max_unique , which returns the index of the
sub-list which has the most unique values.

For example:
index_of_max_unique([[1, 3, 3], [12, 4, 12, 7, 4, 4], [41, 2, 4, 7, 1, 12]]) would return 2 since the sub-list at
index 2 has the most unique values in it (6 unique values).

index_of_max_unique([[4, 5], [12]]) would return 0 since the sub-list at index 0 has the most unique values in it
(2 unique values).

You can assume that neither the list_of_lists nor any of its sub-lists will be empty.

If there is a tie for the max number of unique values between two sub-lists, return the index of the first sub-list
encountered (when reading left to right) that has the most unique values
"""


def index_of_max_unique(num_list):
    index_list = []
    for i in num_list:
        index_list.append(len(set(i)))

    index = max(index_list)
    return index


number_list = [[1, 3, 3], [12, 4, 12, 7, 4, 4], [41, 2, 4, 7, 1, 12], [1, 2, 3, 4, 5, 6]]
number_list1 = [[4, 5], [12], [3, 8]]
print("Number list:", number_list)
output = index_of_max_unique(number_list)
print("The index of sub list containing maximum unique elements is:", output)
