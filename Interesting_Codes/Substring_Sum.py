number = input("Enter a number :- ")
n = len(number)
l = [int(number[0])]
res = int(number[0])
for i in range(1, n):
    l.append((i+1)*int(number[i]) + 10*l[i-1])
    print(res, l[i])
    res += l[i]

print(res)
