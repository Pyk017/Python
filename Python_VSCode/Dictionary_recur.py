# d = {'a': {'b': {'c': 10}}}
# d = {2:{}, 3:{}, 4:{}}
d = {'1': 2.7, '11': 16, '111': {'a': 5, 't': 8}}
def increase_by_one(di):
    for i, j in di.items():
        if type(j) == dict:
            increase_by_one(j)
        else:
            j += 1
            di[i] = j
    return di

res = increase_by_one(d)
print(res)