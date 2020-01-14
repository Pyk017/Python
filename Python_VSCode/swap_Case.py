p = []
a = int(input())
l = [[input(),float(input())] for i in range(a)]
for i in range(0,len(l)):
    p.insert(i,l[i][1])

p.remove(min(p))
result = min(p)

print(result)
print(l)
b = []
for i in l:
    if i[1] is result:
        a[l.index(i)] = 
