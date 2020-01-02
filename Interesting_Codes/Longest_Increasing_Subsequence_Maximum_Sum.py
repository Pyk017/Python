"""
Given an unsorted array of integers, find the Maximum Sum of longest increasing subsequence.
Input : 10 9 2 5 3 7 101 18
Output : 115
Explanation : The longest increasing subsequence is [2, 5, 7, 101], therefore the Sum is 115.
"""


def lis(arr):
    n = len(arr)
    ls = list(arr)
    index = [0]*n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] >= arr[j] and ls[i] < ls[j] + arr[i]:
                ls[i] = ls[j] + arr[i]
                index[i] = j

    i = ls.index(max(ls))
    x = []
    count = 0
    while True:
        x.append(arr[i])
        i = index[i]
        if index[i] == i:
            count += 1
        if count == 2:
            break

    print(x)
    return max(ls)


array = list(map(int, input("Enter elements in the Array :- ").split()))
print('The Maximum Sum of Longest Increasing Sub-Sequence is :- ', lis(array))
