class Record:
    def __init__(self, name, rank):
        self.name = (name)
        self.rank = (rank)

class Rank(Record):
    l = []
    def __init__(self,name, rank):
        super().__init__(name, rank)
        Rank.l = []

    def readValues(self):
        n = int(input("Enter Range of Students :- "))
        print("Enter Name and Rank of Students ")
        for i in range(n):
            temp = input().split(" ")
            self.name.append(temp[0])
            self.rank.append(temp[1])

    def calculate(self):
        Rank.l = sorted(list(zip(self.rank, self.name)))

    def display(self):
        self.readValues()
        self.calculate()
        print("Name of the Highest Rank-Holder is {} with Rank {}".format(Rank.l[0][1], Rank.l[0][0]))

rank = Rank([],[])
rank.display()