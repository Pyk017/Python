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
    if len(arr) < k:
        print("Invalid!")
        return -1

    global_max = 0
    for i in range(k):
        global_max += arr[i]

    current_max = global_max
    for i in range(k, len(arr)):
        current_max += arr[i] - arr[i - k]
        global_max = max(global_max, current_max)

    return global_max


array = list(map(int, input("Enter elements in the array :- ").split()))
key = int(input("Enter window size :- "))
print("Maximum Sum is :- ", max_sum(array, key))
