def my_func(n):
    return lambda a : a * n

a = int(input("Enter First Number!"))
b = int(input("Enter Second Number!"))

lam = my_func(a)

print (lam(b))