"""
University of Washington CSE140 Final Exam 2014
Complete given function such that it returns the sum of the elements in num_list where num_list is the list of numbers.
"""


def sum_of_list(num_list):
    if len(num_list) == 1:
        return num_list[0]
    return num_list[0] + sum_of_list(num_list[1:])


numbers = [44, 23, 77, 11, 89, 3]
print('Sum of elements are :- ', sum_of_list(numbers))
