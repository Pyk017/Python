class Flower:
    def __init__(self):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None
        
    def validate_flower(self):
        self.__flower_name=self.__flower_name.lower()
        if(self.__flower_name=="orchid" or self.__flower_name=="rose" or self.__flower_name=="jasmine"):
            return True
        else:
            return False
    
    def validate_stock(self,required_quantity):
        if required_quantity<=self.__stock_available:
            return True
        else:
            return False
            
    def sell_flower(self,required_quantity):
        if (self.validate_flower()):
            if(self.validate_stock(required_quantity)==True):
                self.__stock_available-=required_quantity
                    
    def check_level(self):
        if self.__flower_name.lower()=="orchid":
            if self.__stock_available>=15:
                return False
            else:
                return True
        elif self.__flower_name.lower()=="rose":
            if self.__stock_available>=25:
                return False
            else:
                return True
        elif self.__flower_name.lower()=="jasmine":
            if self.__stock_available>=40:
                return False
            else:
                return True
        else:
            return False
                
    def get_stock_available(self):
        return self.__stock_available
        
    def set_stock_available(self,stock_available):
        self.__stock_available=stock_available
        
    def get_price_per_kg(self):
        return self.__price_per_kg
    
    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg==price_per_kg
    
    def get_flower_name(self):
        return self.__flower_name
        
    def set_flower_name(self, flower_name):
        self.__flower_name=flower_name
        
florist=Flower()
florist.set_flower_name("ROse")
florist.set_price_per_kg(200)
florist.set_stock_available(27)
florist.validate_stock(4)
florist.sell_flower(4)
print(florist.check_level())
