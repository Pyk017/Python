class Employee:
    raise_amt = 1.04
    num = 0

    def __init__(self, first, last, pay):
        self.first = first  # Instance Variables
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # def get_pay(self):
    #     return self.pay

    def apply_raise_amt(self):
        self.pay = (self.pay * self.raise_amt)
        return self.pay

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
        return cls.raise_amt

    @classmethod
    def set_new(cls,emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, int(pay))


emp_1 = Employee("Prakhar", "Kumar", 50000)  # They are the own unique instances of the employee class
emp_2 = Employee("Yush", "Kumar", 60000)

print (emp_1.fullname())
print (Employee.fullname(emp_2))
# emp_1.apply_raise_amt()
# print (emp_2.pay)
# print(emp_1.pay)
# print (Employee.set_raise_amt(1.10))

emp_str_1 = "John-Snow-65000"
emp_str_2 = "Sansa-Stark-84000"

new_emp_1 = Employee.set_new(emp_str_1)
new_emp_2 = Employee.set_new(emp_str_2)

print(new_emp_1.fullname())
print(new_emp_2.fullname())

print(new_emp_1.pay)
print(new_emp_2.pay)
# print(type(new_emp_2.pay))

print(new_emp_1.apply_raise_amt())
print(new_emp_2.apply_raise_amt())

