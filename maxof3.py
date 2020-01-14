a = int(input("Enter first number:- "))
b = int(input("Enter second number:- "))
c = int(input("Enter third number:- "))
if a > b:
    if a > c:
        print ("{} is greatest among them.".format(a))

    else :
        print ("{} is greatest among them".format(c))

else :
    if b > c:
        print ("{} is greatest among them".format(b))

    else:
        print ("{} is greatest among them".format(c))