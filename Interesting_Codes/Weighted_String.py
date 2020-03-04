"""
In Hackerland every character has a weight. The weight of an English uppercase alphabet A-Z is given below :
A = 1
B = 2*A + A
C = 3*B + B
D = 4*C + C
….
Z = 26*Y + Y

The weight made up of these characters is the summation of weights of each character. Given a total string weight,
determine shortest string of given weight. If there is more than one solution, return the lexicographically smallest of
them. For example, given weight = 25, and the weights of the first few characters of the alphabets are A=1, B=3, C=12,
D=60 it is certain that no letter larger than C is required. Some of the strings with a total weight equal to the target
are ABBBBC, ACC, AAAAAAABBBBBB. The shortest of these is ACC. While any permutation of these characters will have same
, this is the lexicographically smallest of them.

Example
Input
20

Output
AABBC

"""
import string
d = {}
count = 2
j = ''
for i in string.ascii_uppercase:
    if i in 'A':
        d[i] = 1
        j = i
    else:
        d[i] = d[j]*count + d[j]
        j = i
        count += 1

# print(d)
n = int(input('Enter the Number :- '))
temp = ''
ls = []
for i, j in d.items():
    if n < j:
        break
    ls.append((i, j))
# print(ls)

result = ''
for k, l in reversed(ls):
    if n >= l:
        t = n // l
        result += t*k
        n -= t*l

print(result[::-1])