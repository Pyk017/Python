class Employee:
    def __init__(self):
        self.employee_name = None
        self.designation =None

class Customer:
    def __init__(self):
        self.customer_name = None
        self.bill_amount = None

    def purchases(self):
        self.bill_amount=self.bill_amount- self.bill_amount*2/100
        
    def  pays_bill(self,amount):
        print(self.customer_name,"pays bill amount of Rs.",self.bill_amount)
        
class item:
    def __init__(self):
        self.item_id = None
        self.description =None
        self.price_per_unit = None
