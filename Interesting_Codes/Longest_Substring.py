n, x = map(int, input().split())
array = list(map(int, input().split()))
arr_sorted = sorted(array)
i = 0
for i in arr_sorted:
    if i > x:
        break
res = arr_sorted[arr_sorted.index(i) - 1:]
print(res)
