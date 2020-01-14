# 2. Write a class to implement the following:
#  Create a class Employee
# 
#  The Employee class contain properties to store the following
# o ID
# o Name
# o Designation o Department
# o Basic Salary
# o HRA (House Rent Allowance)
# o VA (Vehicle Allowance)
# o NetSalary
#  The Employee class contain methods to perform the following job
# o Store the value of all the properties individually
# o Get the value of all the properties individually
# o Calculate HRA and VA after assigning the value of Basic Salary o Calculate Net Salary after allowances calculations
# o Display all the properties of an employee.

class Employee:
    def __init__(self,id,name,designation,basicSal,hra,va):
        self.id = id
        self.name = name
        self.designation = designation
        self.basicSal = basicSal
        self.hra = hra
        self.va = va        
        # self.netSal = netSal

    def calculate(self):
        return (self.basicSal + self.hra + self.va)

name = input("Enter Name = ")
id = int(input("Enter ID = "))
desig = input("Designation = ")
basicSal = int(input("Basic Salary = "))
hra  = int(input("HRA :- "))
va  = int(input("VA :- "))
emp = Employee(id,name,desig,basicSal,hra,va)
print ("Net Salary is :- {}".format(emp.calculate()))
