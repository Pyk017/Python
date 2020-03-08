from itertools import combinations
import string

input_string = input('Enter a String :- ')
res = [input_string[i:j] for i, j in combinations(range(len(input_string)), 2)]
print(res)
count, result = 0, 0
for i in res:
    if i[0] in string.ascii_lowercase:
        count += 1
    # if "\"" in i:
    #     count += 1
    if "/" in i:
        count += 1
    if ":" in i:
        count += 1
    if count == 3:
        result += 1
        count = 0

print(result)
