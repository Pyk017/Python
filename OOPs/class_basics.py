class Employee:
    raise_amt = 1.04
    num = 0
    def __init__(self,first,last,pay):
        self.first = first  #Instance Variables
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num += 1
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    def get_pay(self):
        return self.pay
    def set_raise_amt(self):
        return (self.pay * Employee.raise_amt)

    def __repr___(self):
        return "In repr"
    def __str__(self):
        return "In str"

emp_1 = Employee("Prakhar","Kumar",50000)  #They are the own unique instances of the employee class
emp_2 = Employee("Yush","Kumar",60000)

emp_2.raise_amt = 1.05

# print (Employee.raise_amt)
# print(emp_2.raise_amt)
# print(emp_1.raise_amt)
# print (emp_1.fullname())
# print (Employee.fullname(emp_2))
# print (emp_1.pay)
# print (Employee.get_pay(emp_2))
# print (emp_1.set_raise_amt())
# print(Employee.set_raise_amt(emp_2))
# print (Employee.num)Employee
print(repr(emp_1))
print(str(emp_1))
print(emp_1)
print(Employee.__repr___(emp_1))
print(emp_2.__str__())
# print(emp_1.__repr__())/