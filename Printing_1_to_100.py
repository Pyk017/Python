def even(m, n):
    if m == n:
        print(n) if m % 2 != 0 else print(n * 2)
    else:
        if m % 2 == 0:
            print(m*2)
        else:
            print(m)
        even(m + 1, n)


even(1, 100)
