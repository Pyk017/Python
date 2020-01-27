"""
Given two lists, both having String elements, write a python program using python lists to create a new string as per
the rule given below:
The first element in list1 should be merged with last element in list2, second element in list1 should be merged with
second last element in list2 and so on. If an element in list1/list2 is None, then the corresponding element in the
other list should be kept as it is in the merged list.

            Sample Input	                                                    Expected Output
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']	                    “An apple a day keeps the doctor away"

"""


def merge_list(list1, list2):
    resultant_data = ''
    # print(list(zip(list1, list2[::-1])))
    for i, j in zip(list1, list2[::-1]):
        if not i:
            resultant_data += j + ' '
        elif not j:
            resultant_data += i + ' '
        else:
            resultant_data += i + j + " "

    return resultant_data.rstrip()


# Provide different values for the variables and test your program
# list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
# list2=['y','tor','e','eps','ay',None,'le','n']
# list1=['T', 'sk', None, 'bl']
# list2=['ue', 'is', 'y', 'he']
list_1 = ['The', 's', 'ris', 'in', None, 'ea']
list_2 = ['st', 'the', None, 'es', 'un', None]
merged_data = merge_list(list_1, list_2)
print(merged_data)
