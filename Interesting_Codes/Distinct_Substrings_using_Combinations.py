from itertools import combinations
input_string = input('Enter a string :- ')
res = [input_string[i:j] for i, j in combinations(range(len(input_string) + 1), 2)]
print(res)
