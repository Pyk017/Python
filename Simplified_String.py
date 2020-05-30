# Write recursive function simplified(string) that returns a string similar to the input string but with all consecutive duplicates characters removed.
# For Example : simplified('AABBCCCBBDD')
# ANS: 'ABCBD'
# simplified('GGABAA')
# ANS: 'GABA'

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
