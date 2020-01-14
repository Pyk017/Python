class op:
    def __init__(self,name,age,clg):
        self.n = name
        self.a = age
        self.c = clg

    def func(self):
        print ("My name is {} of {} and my age is :- {}".format(self.n,self.c,self.a))


x = "Prakhar Kumar Kashyap"
p = op(x,20,"PSIT")
p.func()
y = "Yush Kumar Kashyap"
p = op(y,20,"PSIT")
p.func()
p.clg = "IIT"
print (p.clg)