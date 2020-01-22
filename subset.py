def subsets(array):
	sub = [0]*(len(array))
	helper(array, sub, 0)
	
def helper(array, subset, i):
	if i == len(array):
		print(subset)
	else:
        subset[i] = 0
		helper(array, subset, i+1)
		subset[i] = array[i]
		helper(array, subset, i+1)
		

print(subsets([1, 2, 3]))