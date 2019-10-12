class Juggler:
    def __init__(self,name):
        self.__name=name

    def juggles(self,jugglingitem):
        self.__jugglingitem=jugglingitem
        print(self.__name ,"is juggling with ",self.__jugglingitem)

class JugglingItem:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
s=JugglingItem("Balls")
Jack=Juggler("Jack")
Jack.juggles(s.get_name())
