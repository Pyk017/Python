n = int(input("Enter number of Students :- "))

#l = [[input("Enter Name of Student {} :- ".format(i+1)),input("Enter Marks of Student {} :- ".format(i+1))] for i in range(n)]
ll = []
l = []

for i in range(n):
    ll.insert(1,input("Enter Name of Student {}".format(i+1)))
    ll.insert(0,input("Enter Score of Student {}".format(i+1)))
    l.insert(i,)
print(l)
l = sorted(l)
print(l)