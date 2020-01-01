from collections import Counter


def check_anagram(data1, data2):
    # if len(data1) != len(data2):
    #     return False
    # else:
    #     for i in data1:
    #         if i not in data2 or data1.inde:
    #             return False
    #
    #     return True
    # print(Counter(data1), Counter(data2))
    return Counter(data1) == Counter(data2)


str1 = input("Enter First String :- ")
str2 = input("Enter Second String :- ")
print("Two Strings are Anagram!") if check_anagram(str1, str2) else print("Two Strings are not Anagram!")

