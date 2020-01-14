a = int(input("Enter a number"))
e,o,b = 0,0,str(a)
for i in b:
    if int(i)%2 is 0:
        e +=1
    else:
        o +=1

print ("Number of even number are {}".format(e))
print ("Number of odd number are {}".format(o))
    