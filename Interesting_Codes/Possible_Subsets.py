def subsets(array):
    subset = [0]*len(array)
    helper(array, subset, 0)


def helper(array, subset, i):
    if i == len(array):
        print(subset)

    else:
        subset[i] = []
        helper(array, subset, i+1)
        subset[i] = array[i]
        helper(array, subset, i+1)


arr = list(map(int, input("Enter array elements :- ").split()))
subsets(arr)
