"""
Dia, Sam, and Robert are the three students of a same class. You know their marks in ‘N’ subjects. Your job is to find
their ranks according to their score.

Input

N, integer denoting number of subjects.
3 array of integers, denoting marks of Dia, Sam and Robert respectively in N subjects.

Output
Ranks

Example :
Input
3
23 34 23
32 53 23
55 22 67

Output
3 2 1

"""


subs = int(input('Enter totals numbers of Subjects :- '))
rank = [0]*3
temp = list()
for i in range(3):
    temp.append(sum(list(map(int, input().split()))))

t = sorted(temp, reverse=True)
count = 1
for i in t:
    rank[temp.index(i)] = count
    count += 1

print(rank)
