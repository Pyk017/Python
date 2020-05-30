def user_reverse(ls, i, size):
    if i == size:
        return ls[::-1]
    else:
        if type(ls[i]) == list:
            ls[i] = user_reverse(ls[i], 0, len(ls[i]))
        return user_reverse(ls, i+1, len(ls))

def deep_reverse(ls):
    return user_reverse(ls, 0, len(ls))


# ls = [1, [3, 4], 9]
ls = [1, 2, [3, 4], [[5]], [6, [7, 8], 9]]
print(deep_reverse(ls))
