#  check = lambda x: True if x[0] >= x[1] else False


def is_desc(ar):
    if len(ar) == 2:
        if ar[0] >= ar[1]:
            return True
        return False
    else:
        if is_desc(ar[:-1]) and is_desc(ar[-2:]):
            return True
        return False



arr = list(map(int, input().split()))
res = is_desc(arr)
print(res)