string = input("Enter String :- ")
div = int(input("Enter Separator :- "))
k,l = div,[]
for i in range(div):
    l.append(list(string[:k]))
    string = string[k:]
l2 = []
for i in l:
    for j in i:
        if i.count(j) >= 2:
                i.remove(j)
                break
    
    l2.append("".join(i))    

for i in l2:
        print(i)

# # print(l)
# n = int(input())
# s = set()
# for i in range(n):
#     # name = input()
#     s.add(input())

# print(len(s))
