class Ticket:
    counter = 0
    def __init__(self, passenger_name, source, destination):
        self.__passenger_name = passenger_name.upper()
        self.__source = source.upper()
        self.__destination = destination.upper()
        self.__ticket_id = None

    def validate_source_destination(self):
        if (self.__source.upper() in 'DELHI') and (self.__destination.upper()=="MUMBAI" or self.__destination.upper()=="CHENNAI" or self.__destination.upper()=="PUNE" or self.__destination.upper()=="KOLKATA"):
            return True
        return False

    def generate_ticket(self):
        if self.validate_source_destination() :
            Ticket.counter += 1
            if Ticket.counter <= 9:
                self.__ticket_id = self.__source[0] + self.__destination[0] + '0' + str(Ticket.counter)
            else:
                self.__ticket_id = self.__source[0] + self.__destination[0] + str(Ticket.counter)

        

    def get_ticket_id(self):
        return self.__ticket_id

    def get_passenger_name(self):
        return self.__passenger_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

ticket = Ticket("Prakhar Kumar", "Delhi", "Kolkata")
ticket.generate_ticket()
if ticket.get_ticket_id() is None:
    print ("Invalid data!")
else:
    print ("{} {} {} {}".format(ticket.get_passenger_name(), ticket.get_source(), ticket.get_destination(), ticket.get_ticket_id()))
