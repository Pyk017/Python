def grouping(string):
    d = {i: [] for i in range(1, 27)}
    for i in string:
        if ord(i) < 98:
            d[ord(i) - 64].append(i)
        else:
            d[ord(i) - 96].append(i)

    res = ''
    i = 1
    j = 26
    while len(res) != len(string) and i < 27 and j > 0:
        while not d[i]:
            i += 1
        res += ''.join(d[i])
        i += 1
        if len(res) == len(string):
            break
        # print(res, i)
        while not d[j]:
            j -= 1
        res += ''.join(d[j])
        j -= 1 
        # print(res, len(res))
    return res
         

string = input()
res = grouping(string)
print(res)