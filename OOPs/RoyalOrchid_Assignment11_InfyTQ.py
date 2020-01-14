class Flower:
    listing = {'Orchid':15, 'Rose':25, 'Jasmine':40}

    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None

    def get_flower_name(self):
        return self.__flower_name

    def set_flower_name(self, flower):
        self.__flower_name = flower

    def get_price_per_kg(self):
        return self.__price_per_kg

    def set_price_per_kg(self, price):
        self.__price_per_kg = price

    def get_stock_available(self):
        return self.__stock_available

    def set_stock_available(self, stock):
        self.__stock_available = stock

    def validate_flower(self):
        if self.__flower_name in Flower.listing:
            return True
        return False

    def validate_stock(self, required_quantity):
        if required_quantity <= self.__stock_available:
            return True
        return False

    def sell_flower(self, required_quantity):
        if self.validate_flower() and self.validate_stock(required_quantity):
            self.__stock_available -= required_quantity
            self.set_stock_available(self.__stock_available)

    def check_level(self):
        for i, j in Flower.listing.items():
            if self.__flower_name in i:
                return True if self.__stock_available < j else False

florist = Flower()
florist.set_flower_name('Orchid')
# print (florist.get_flower_name())
florist.set_price_per_kg(1200)
florist.set_stock_available(50)
print ("{} {} {}".format(florist.get_flower_name(), florist.get_stock_available(), florist.get_price_per_kg()))
print (florist.validate_flower())
print (florist.validate_stock(42))
florist.sell_flower(30)
print (florist.check_level())

