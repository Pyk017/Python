a = int(input("Enter initial number:- "))
b = int(input("Enter final number:- "))
k = 0
for i in range(a , b + 1):
    count = 0
    for j in range(1 , (i+1)):
        if(i%j == 0):
            count += 1
            
    if(count == 2):
        print(i," is Prime Number")
            
             


    