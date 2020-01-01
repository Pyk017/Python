n1 = list(map(int, input("Input First Number :- ")))
n2 = list(map(int, input("Input Second Number :- ")))
n3 = list(map(int, input("Input Third Number :- ")))
result, maxi = '', 0
for i in range(len(n1)):
    result += str(min(n1[i], n2[i], n3[i]))
    if maxi < max(n1[i], n2[i], n3[i]):
        maxi = max(n1[i], n2[i], n3[i])

print ("Your PIN Generated is :- ",str(maxi) + result)



