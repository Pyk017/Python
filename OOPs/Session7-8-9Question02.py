class Details:
    def __init__(self, name, address, telno, rent):
        self.name = name
        self.address = address
        self.telno = telno
        self.rent = rent

    def display(self):
        print("Name of the Customer is :- {}".format(self.name))
        print("Address of the Customer is :- {}".format(self.address))
        print("Phone Number is :- {}".format(self.telno))
        print("Rent of the Customer is :- {}".format(self.rent))

class Bill(Details):
    amt = 0
    def __init__(self, name, address, telno, rent, n):
        super().__init__(name, address, telno, rent)
        self.n = n

    def calculate(self):
        if self.n <= 100:
            Bill.amt = self.rent

        elif self.n > 100 and self.n <= 200:
            Bill.amt = self.n*0.60 + self.rent

        elif self.n > 200 and self.n <= 300:
            Bill.amt = self.n*0.80 + self.rent

        else:
            Bill.amt = self.n + self.rent

    def show(self):
        self.calculate()
        self.display()
        print("Total Bill of the Customer is :- {}".format(Bill.amt))

name = input("Enter Name of the Customer :- ")
address = input("Enter Address :- ")
telno = int(input("Enter telephone Number :- "))
rent = int(input("Enter rent of the Customer :- "))
call = int(input("Enter total calls made by the Customer :- "))

bill = Bill(name, address, telno, rent, call)
print("\nYour Details are as follows :- ")
bill.show()

