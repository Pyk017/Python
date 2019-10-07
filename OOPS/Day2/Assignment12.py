class Bill:
    def __init__(self, bill_id, patient_name):
        self.__bill_id = bill_id
        self.__patient_name = patient_name
        self.__bill_amount = 0

    def calculate_bill_amount(self, consultation_fees, quantity_list, price_list):
        self.__bill_amount = consultation_fees
        for i, j in list(zip(quantity_list, price_list)):
            self.__bill_amount += i * j

    def get_bill_id(self):
        return self.__bill_id

    def get_patient_name(self):
        return self.__patient_name

    def get_bill_amount(self):
        return self.__bill_amount

bill = Bill(22771, "Prakhar")
quantity = [7, 8, 9, 6]
price = [20, 50, 60, 80]
fees = 150
bill.calculate_bill_amount(fees, quantity, price)
print (bill.get_patient_name())
print (bill.get_bill_id())
print (bill.get_bill_amount())

