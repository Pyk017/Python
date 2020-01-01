level = int(input("Enter Total levels in the Hill Pattern :- "))
head = int(input("Enter Weight of the Head Level :- "))
increament = int(input("Enter weight increament of subsequent level :- "))
result = 0
for i in range(1, level+1):
    result += (head * i)
    head += increament

print("The Total Weight of the Hill Pattern is :- ",result)