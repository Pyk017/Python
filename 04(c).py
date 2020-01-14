a = input("Enter a String :- ")
b = ""
l = a.split(' ')
for i in sorted(l):
    if b.count(i) is 0:
        b += i
        b += " "

b = b[:-1]
print ("Sorted String is :- {}".format(b))
