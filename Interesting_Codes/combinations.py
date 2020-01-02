import itertools
n, a, b = list(map(int, input("Enter N, A and B :- ").split()))
l = list(dict(zip(itertools.count(a), range(b - a + 1))))
flag = False
new_l = []
j = 0
for i in range (2, n // min(l) + 1):
    it = list(itertools.combinations_with_replacement(l, i))
    for j in it:
        if sum(j) % n == 0:
            flag = True
            break

    if flag :
        new_l.append(j)
        break

if not new_l:
    print ('No!')
else:
    print (' '.join(map(str, new_l[0])))
    # print("Yes!\n", sorted(new_l, key=lambda x: len(x))[0])2