def recur(n, count=0):
    if n == 1:
        return count
    else:
        if n % 2 == 0:
            return recur(n // 2, count + 1)
        else:
            return recur((3 * n) + 1, count + 1)
    

n = int(input())
res = recur(n)
print(res)
