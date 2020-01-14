# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product
from itertools import permutations
# a = input()
# b = input()
# l1 = a.split(" ")
# l2 = b.split(" ")
# for i in l1:
#     l1[l1.index(i)] = int(i)

# for i in l2:
#     l2[l2.index(i)] = int(i)

# l = [l1,l2]
# ll = list(product(*l))
# for i in ll:
#     print(i,end=" ")
stri = "" 
a = input()
m = a.index(" ")
b = a[:m]
c = int(a[m+1:])
l = sorted(list(permutations(b,c)))
for i in l:
    for j in range(c):
        stri += i[j]

    print (stri)
    stri = ""
    # print(l[l.index(i)][0] + l[l.index(i)][1])
