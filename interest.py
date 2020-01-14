p = int(input("Enter a principle value:- "))
r = int(input("Enter rate of interest applied :- "))
t = int(input("Enter time in years :- "))
interest = (p*r*t) / 100
print("The Interest over your Principle value is {}".format(interest))