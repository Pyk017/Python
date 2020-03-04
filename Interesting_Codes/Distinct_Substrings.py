def distinct_substring(string):
    result = set()
    for i in range(len(string)+1):
        for j in range(i+1, len(string)+1):
            result.add(string[i:j])
            print(string[i:j])

    return result


input_string = input('Enter String :- ')
print(distinct_substring(input_string))
