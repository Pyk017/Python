# 1. Write a program to implement a class to store details related to a Student. The Student class contains the following information of a student.
#  rollno
#  name
#  address
#  father name
#  age
#  contact number
#  nationality
#  branch
#  section
# Then after create an instance of the class and print all the details of a student after assigning the values.
class Student:
    def __init__(self,name,rn,add,fname,age,contact,nation,branch,sec):
        self.name = name
        self.rn = rn
        self.add = add
        self.fname = fname
        self.age = age
        self.contact = contact
        self.nation = nation
        self.branch = branch
        self.sec = sec

student = Student("Prakhar Kumar",22771,"Latouche Road","Suresh Kumar",21,8874109902,"Indian","CSE","E")
print("Name is :- {}".format(student.name))
print("Address is :- {}".format(student.add))
print("Roll No. is :- {}".format(student.rn))
print("Father's Name is :- {}".format(student.fname))
print("Age :- {}".format(student.age))
print("Contact Number :- {}".format(student.contact))
print("Nationality :- {}".format(student.nation))
print("Branch :- {}".format(student.branch))
print("Section :- {}".format(student.sec))

