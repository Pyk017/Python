def remove_dublicates(value):
    # result = ''.join(list(dict.fromkeys(value)))
    result = []
    for i in value:
        if i not in result:
            result.append(i)

    return ''.join(result)


print(remove_dublicates('1123344556666ababzzz@@@123#*#*'))
