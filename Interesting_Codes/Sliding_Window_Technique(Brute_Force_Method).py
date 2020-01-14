<<<<<<< HEAD
"""
Given an array of integers of size 'n'. Our aim is to calculate the maximum sum of 'k' consecutive elements in the
array.
Input : [100, 200, 300, 400] k = 2
Output : 700
Input : [1, 4, 2, 10, 23, 3, 1, 0, 20] k = 4
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.
"""


def max_sum(arr, k):
    max_global = 0
    for i in range(len(arr) - k + 1):
        current_max = 0
        for j in range(k):
            current_max += arr[i + j]

        max_global = max(max_global, current_max)

    return max_global


array = list(map(int, input("Enter elements in the array :- ").split()))
key = int(input("Enter window size :- "))
print("Maximum Sum is :- ", max_sum(array, key))
=======
"""
Given an array of integers of size 'n'. Our aim is to calculate the maximum sum of 'k' consecutive elements in the
array.
Input : [100, 200, 300, 400] k = 2
Output : 700
Input : [1, 4, 2, 10, 23, 3, 1, 0, 20] k = 4
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.
"""


def max_sum(arr, k):
    max_global = 0
    for i in range(len(arr) - k + 1):
        current_max = 0
        for j in range(k):
            current_max += arr[i + j]

        max_global = max(max_global, current_max)

    return max_global


array = list(map(int, input("Enter elements in the array :- ").split()))
key = int(input("Enter window size :- "))
print("Maximum Sum is :- ", max_sum(array, key))
>>>>>>> Python repo committed
