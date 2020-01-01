string = input("Enter a String :- ").lower().split(" ")
storage, result = 0, ''
for s in string:
    for i in range(len(s)//2):
        storage += abs(ord(s[i]) - ord(s[len(s) - i - 1]))
    if len(s) % 2 != 0:
        storage += ord(s[len(s) // 2]) - 96
    result += str(storage)
    storage = 0

print (result)
