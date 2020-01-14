# Given an unsorted integer array, find the first missing positive number integer.
# Example : [1, 2, 0] return 3.
# [3, 4, 1, -1] return 2.
# [-8, -7, -6] return 1.


def missing(a):
    m = max(a)
    if m < 0 or len(a) == 1:
        return 1
    elif len(a) == 1:
        if a[0] < 0:
            return 1
        else:
            return a[0] + 1
    else:
        c = [0] * (m + 2)
        for i in a:
            c[i] += 1
        res = 0
        for i in c:
            if i == 0:
                res = c.index(i)
                break

        return res


lis = list(map(int, input("Enter array elements :- ").rstrip().split()))
print("Missing element is :- ", missing(lis))
