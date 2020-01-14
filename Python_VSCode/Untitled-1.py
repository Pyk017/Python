a = int(input("Enter how many terms required ?"))
b = 0
c = 1 
count = 0
d = 0
if a <= 0:
    print ("Enter valid Positive Integer!")
elif a == 1:
    print ("Your Fibonacci Sequence is as Follows :- ")
    print (b,end=" ,")
else:
    print ("Your Fibonacci Sequence is as Follows :- ")
    while count < a:
        print (b,end = ",")
        d = c + b
        b = c
        c = d
        count +=1

