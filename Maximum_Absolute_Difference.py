def max_diff(a):
    maxi = 0
    for i in range(len(a) - 1):
        c = abs(a[i] - a[i+1])
        if c > maxi:
            maxi = c

    return maxi


print(max_diff([0, 0, 0, 0]))
print(max_diff([0, 1, 2, 3]))   # 0 - 1 = 1; 1 - 2 = 1; 2 - 3 = 1; Maximum among them is 1.
print(max_diff([5, 10, 20, 40]))  # 5 - 10 = 5; 10 - 20 = 10; 20 - 40 = 20, Maximum among them is 20.
print(max_diff([-5, 5, 7, 11]))
print(max_diff([7, 8, 3, 5, 9]))
