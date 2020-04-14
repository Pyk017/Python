# Write a python program to calculate the value of each elements in the sequence. 
# Using the following recursion : Cn = Cn-1 - 3Cn-2 + 2Cn-3 with c1 = 2, c2 = -3, c3 = 4.

def recur(n):
    if n == 1:
        return 2
    elif n == 2:
        return -3 
    elif n == 3:
        return 4
    else:
        return recur(n - 1) + 3 * recur(n - 2) + 2 * recur(n - 3)

num = int(input())
print(recur(num))
