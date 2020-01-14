from collections import Counter
n = input("Enter Input 1 :- ") + input("Enter Input 2 :- ") + input("Enter Input 3 :- ") + input("Enter Input 4 :- ")
count = dict(Counter(list(map(int, n))))
count = sorted(count.items(), key=lambda x: (x[0], x[1]))
count = sorted(count, key = lambda x: x[1])
print ("The Most Frequent Digit is :- ",count[-1][0])