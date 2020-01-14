import pickle
import os
import pathlib

class Account:
    accNo = 0
    name = ' '
    deposit = 0
    type = ' '

    def createAccount(self):
        self.accNo = int(input("Enter the Account Number :- "))
        self.name = input("Enter Name of the Account Holder :-  ")
        self.deposit = int(input("Enter the Initial amount( >= 500 for Saving or >=1000 for Current) :- "))
        self.type = input("Enter the type of the Account [C/S] :- ")
        print ("\n\nAccount Created")

    def showAccount(self):
        print ("Account Holder Name is :- {}".format(self.name))
        print("Your Account Number is :- {}".format(self.accNo))
        print("Type of Account is :- {}".format(self.type))
        print("Balance is :- {}".format(self.deposit))

    def modifyAccount(self):
        print ("Account Number :- {}".format(self.accNo))
        self.name = input("Modify Account Holder Name :- ")
        self.type = input("Modify type of Account :- ")
        self.deposit = int(input("Modify Deposit :- "))

    def depositAmount(self,amount):
        self.deposit += amount

    def withdrawAmount(self,amount):
        self.deposit -= amount

    def report(self):
        print ("{}  {}  {}  {}".format(self.accNo,self.name,self.type,self.deposit))

    def getAccountNumebr(self):
        return self.accNo

    def getAccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.deposit


def Introduction():
    print ("\t\t\t\t*******************************")
    print ("\t\t\t\t\tBank Management System")
    print("\t\t\t\t*******************************")

    print("\t\t\t\tBrought to you by :- ")
    print("\t\t\t\tPrakhar Kumar Kashyap")


def writeAccount():
    account = Account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("account.data")
    if file.exists():
        infile = open



