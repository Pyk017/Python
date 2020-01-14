a = int(input("Enter a number"))
b = int(input("Enter another number"))
count,c = 0,0
for i in range (a , b+1):
    c = i//2
    for j in range (2, c + 1):
        if (i%j) is 0:
            break

    if j is c:
        print(i)
