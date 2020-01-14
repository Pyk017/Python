n = int(input("ENter numbers needed :-"))
a,b = 0,1
print (a,b,end=" ")
while(n-2):
    c = a + b
    a = b
    b = c
    print(c,end=" ")
    n -= 1