class User:
    def __init__(self):
        self.en()
    def en(self):
        self.na=input("Enter your name:")
        if self.na==a.name:
            a.app()
        elif self.na==b.name:
            b.app()
        elif self.na==c.name:
            c.app()
        else:
            print("Wrong username")
            self.en()
class Bank:

    acno=12345
    acclist={}
    def __init__(self,name,amount,pin):
        Bank.acno+=1
        self.acno=Bank.acno
        self.name=name
        self.balance=amount
        self.pin=pin
        self.printDetail()
    
    def printDetail(self):
        print(f'Account number {self.acno}')
        print(f'Name {self.name}')
        print(f'Balance {self.balance}')
        print(f'Pin {self.pin}')
        print()
    
    def app(self):
        print("Enter your detail to login")
        ac=int(input("Enter your account number:"))
        pin=int(input("Enter your pin:"))
        if self.acno==ac and self.pin==pin:
            print("Welcome")
            self.menu()
        else:
            print("You have entered wrong details")
            self.app()
    def menu(self):
        print('1)Check Balance \n2)Change PIN \n3)Transfer Amount \n4)Exit')
        n=int(input("Enter your choice:"))
        if n==1:
            print(f'Bank Balance:{self.balance}')
        elif n==2:
            self.ChangePin()
            print("PIN change successfully")
            self.app()
        elif n==3:
            self.TransferAmount()
        elif n==4:
            exit
        self.menu()

    def ChangePin(self):
        pn=int(input("Enter your current PIN:"))
        if pn==self.pin:
            self.pin=int(input("Enter your new PIN:"))
        else:
            print("You have entered wrong PIN")
    
    def TransferAmount(self):
        pn=int(input("Enter your PIN:"))
        if pn==self.pin:
            am=int(input("Enter amount to transfer:"))
            if am>self.balance:
                print("Balance is Low")
                self.menu()
            ac=int(input("Enter Account Number of reciver:"))
            if ac==self.acno:
                print("You have entered your own Account number")
                self.menu()
            rac=Bank.acclist[ac]
            self.balance=self.balance-am
            rac.balance=rac.balance+am
            print("Amount transfered successfully")
        else:
            print("You have entered wrong PIN")
    
    def addAccountToList(self,Variable):
        Bank.acclist.update({self.acno:Variable})
    
a=Bank("Vansh",12000,2005)
a.addAccountToList(a)
b=Bank("Sugam",10000,5432)
b.addAccountToList(b)
c=Bank("Dhrumil",23000,9876)
c.addAccountToList(c)
Us=User()