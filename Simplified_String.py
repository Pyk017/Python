def simplified(s, res = []):
    if len(s) == 1:
        res.append(s[0])
        return res
    else:
        temp = simplified(s[1:], res)
        if s[0] != temp[-1]:
            res.append(s[0])
        return res


string = input()
res = ''.join(simplified(string)[::-1])
print(res)
