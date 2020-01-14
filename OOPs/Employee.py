class Employee :
    def __init__(self,fname,lastname,pay):
        self.fname = fname
        self.lastname = lastname
        self.pay = pay
        self.email = fname + "."+ lastname + "@gmail.com"

    def fullname(self):
        return "{} {}".format(self.fname,self.lastname)

    def full_details(self):
        return "Name = {} {}\n Email = {}".format(self.fname,self.lastname,self.email)

    def payment(self):
        return "Name = {} {}\n Payment = {}".format(self.fname,self.lastname,self.pay)

obj = Employee("Prakhar","Kumar","60000")

print (obj.fullname())
print (obj.full_details())
print (obj.payment())



# Prakhar me = Prakhar()

# while (me.alive()):
#     me.sleep()
#     continue
#     me.eat()
#     me.practice()
#     me.work()
#     me.make_contibution_to_my_family()
#     me.make_contibution_to_society()
#     me.be_Positive()
#     me.be_Productive()
#     me.do_literally_anything(
