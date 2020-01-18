"""
Tom is working in a shop where he labels item. Each item is labelled with a number between num1 and num2(both inclusive)
Since Tom is also a natural mathematician, he likes to observe pattern in numbers. Tom could observe that some of these
label numbers are divisible by other label numbers.
Write a Python function to find out those label numbers that are divisible by another number and display how many such
label numbers are there totally.
Note :- Consider only distinct label Numbers. The list of those label Numbers should be considered as a set.
"""


def check_numbers(num1, num2):
    num_list = set()
    for i in range(num1, num2+1):
        for j in range(num1, num2+1):
            if i != j and i % j == 0:
                num_list.add(i)

    return [list(num_list), len(num_list)]


print(check_numbers(2, 20))
