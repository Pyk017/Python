a = int(input("Enter a number"))
b = int(input("Enter another number"))
for j in range(a,b+1):
    arms = 0
    for i in str(j):
        arms += int(i)**3

    if (arms) is j:
        print (j)


