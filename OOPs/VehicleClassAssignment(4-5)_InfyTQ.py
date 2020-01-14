class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, vehicle_cost, premium_amount):
        self.__vehicle_cost = vehicle_cost
        self.__vehicle_type = vehicle_type
        self.__vehicle_id  = vehicle_id
        self.__premium_amount = premium_amount

    def set_Vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def get_Vehicle_id(self):
        return self.__vehicle_id

    def set_Vehicle_type(self, vehicle_type):
        self.__vehicle_type = vehicle_type
        
    def get_Vehicle_type(self):
        return self.__vehicle_type

    def set_Vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost = vehicle_cost
        
    def get_Vehicle_cost(self):
        return self.__vehicle_cost

    def set_premium_amount(self, premium_amount):
        self.__premium_amount = premium_amount
        
    def get_premium_amount(self):
        return self.__premium_amount


    def calculate_premium(self):
        if (self.__vehicle_type).upper() == "TWOWHEELER":
            self.__premium_amount = 0.2 * self.__vehicle_cost
            self.__vehicle_cost += self.__premium_amount

        elif (self.__vehicle_type).upper() == "FOURWHEELER":
            self.__premium_amount = 0.6 * self.__vehicle_cost
            self.__vehicle_cost += self.__premium_amount

        else:
            print("Invalid Input")

    def display_vehicle_details(self):
        print("Vehicle ID : {}".format(self.__vehicle_id))
        print("Vehicle Type : {}".format(self.__vehicle_type))
        print("Vehicle Cost : {}".format(self.__vehicle_cost))
        print("Vehicle Premium Amount : {}".format(self.__premium_amount))


veh1 = Vehicle(22771,"TwoWheeler",52000,34)
veh1.calculate_premium()
veh1.display_vehicle_details()