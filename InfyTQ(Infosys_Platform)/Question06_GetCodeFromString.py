string = sum(list(map(len, input("Enter Your String :- ").split(" "))))
while string >= 10: string = sum(list(map(int, str(string))))
print("The Single-digit Numeric PIN is :- ",string)