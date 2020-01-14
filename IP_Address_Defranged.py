ip = input("Enter IP Address :- ")
res = ''
for i in ip:
    if i in '.':
        res += '[.]'
    else:
        res += i

print("New IP is :- ", res)
