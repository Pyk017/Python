def details():
    ls = []
    ls.append(input('Enter First Name :- '))
    ls.append(input('Enter Second Name :- '))
    ls.append(input('Enter User Id :- '))
    print("Name : {} {} and User id: {}".format(*ls))

def numbers():
    a, b = map(int, input('Enter two numbers :- ').split())

    def display():
        print("First Number is : ", a)
        print("Second Number is : ", b)

    def add():
        print('Addition of two Numbers is :- ', a + b)

    def mul():
        print('Multiplicaiton of two Numbers is :- ', a * b)

    display()
    add()
    mul()

details()
numbers()
    


