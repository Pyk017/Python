def sub_array(ar, w):
    n = len(ar)
    ls = [[0 for _ in range(w+1)] for _ in range(n+1)]

    for i in range(len(ls)):
        for j in range(len(ls[i])):
            if j == 0:
                ls[i][j] = 1
            elif i == 0 and j != 0:
                ls[i][j] = 0
            elif j < ar[i-1]:
                ls[i][j] = ls[i-1][j]
            else:
                ls[i][j] = ls[i-1][j-ar[i-1]] + ls[i-1][j]

    print(ls)
    return ls[n][w]


array = list(map(int, input("Enter array elements :- ").split()))
k = int(input("Enter Sum :- "))
result = sub_array(array, k)
print(result)
