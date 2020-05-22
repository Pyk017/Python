for _ in range(int(input())):
    string = input()
    ls = string.split('.')[::-1]
    result = '.'.join(ls)
    print(result)