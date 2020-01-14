class Employee:
    amount = 1.04
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName  = lastName
        self.pay = pay
        self.email = self.firstName + "." + self.lastName +"@company.com"
    @classmethod
    def create(cls, empstr):
        first, last, pay = empstr.split(" ")
        return cls(first, last, int(pay))

    def fullName(self):
        return "{} {}".format(self.firstName, self.lastName)

    def apply_amount(self):
        return (self.pay * Employee.amount)


class Developer(Employee):
    def __init__(self, firstName, lastName, pay, prog_lang):
        super().__init__(firstName, lastName, pay)
        self.prog_lang = prog_lang

    @classmethod
    def create2(cls, empstr):
        first, last, pay, prg = empstr.split(" ")
        return cls(first, last, int(pay), prg)

class Manager(Employee):
    def __init__(self, firstName, lastName, pay, emp=None):
        super().__init__(firstName, lastName, pay)
        if emp is None:
            self.emp = None
        else:
            self.emp = emp

    @classmethod
    def create3(cls, empstr):
        first, last, pay = empstr.split(" ")
        return cls(first, last, int(pay), [])

    def add_emp(self, empNew):
        if empNew not in self.emp:
            self.emp.append(empNew)

    def remove_emp(self, empNew):
        if empNew in self.emp:
            empNew.remove(self.emp)

    def print_emp(self):
        for i in self.emp:
            print("-->",i.fullName())

dev1 = input("Enter Full Name with Payment and Programming Language of First Developer :- ")
dev2 = input("Enter Full Name with Payment and Programming Language of Second Developer :- ")

dev_1 = Developer.create2(dev1)
dev_2 = Developer.create2(dev2)
# dev_1 = Developer("Prakhar","Kumar",500000,"Python")
# dev_2 = Developer("Yush","Kashyap",650000,"JavasScript")
mgr = input("Enter Full Name with Payment of Manager :- ")
mgr_1 = Manager.create3(mgr)


print(dev_1.fullName())
print(dev_1.email)
print(dev_1.pay)
print(dev_1.apply_amount())
print(dev_1.pay)

print()
print(dev_2.fullName())
print(dev_2.email)
print(dev_2.pay)
print(dev_2.apply_amount())
print(dev_2.pay)

print()
print(mgr_1.fullName())
print(mgr_1.email)
print(mgr_1.pay)
print(mgr_1.apply_amount())
print(mgr_1.pay)

mgr_1.add_emp(dev_1)
mgr_1.add_emp(dev_2)
mgr_1.print_emp()
