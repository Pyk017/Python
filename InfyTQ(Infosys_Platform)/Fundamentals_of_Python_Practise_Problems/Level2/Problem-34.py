"""
Write a recursive function which True if the input is well-formatted and with respect to the list labels. Else it should
return False.

We say that an list is well-formatted with respect to the labels if:
1. input item is a list.
2. input item have a length of at least two.
3. input's first item is in the list labels.
4. each of the remaining items in input is either a well-formatted list or a string.

Sample input	                                                        Expected output
input item	                                list label
['VP', ['V', 'eat']]	                    ['VP', 'V']                     True
['NP', ['N', 'a', 'or', 'b'], 'c']	        ['NP', 'V', 'N']	            True
[1, [2, 'oui', [1, 'no']], 'no']	        [1,2]	                        True
['VP', ['V', 'eat']]	                    ['VP']	                        False
['VP', ['V']]	                            ['VP', 'V']	                    False
"""


def check_well_formatted(input_list, list_label):
    if type(input_list) is not list and len(input_list) < 2 and input_list[0] not in list_label and \
            (not check_well_formatted(input_list[1:], list_label) or all(list(map(lambda x: x == str(x), input_list[1:])))):
        return False

    return True


input_list1 = ['VP', ['V', 'eat']]
list_label1 = ['VP', 'V']
result = check_well_formatted(input_list1, list_label1)
if result is True:
    print("Well formatted")
else:
    print("Not Well formatted")
