a = input("Enter a String :- ")
d = {}

for i in a:
    d[i] = d.get(i,0) + 1

for j in sorted(d) :
    print ("{} : {}".format(j,d[j]))