class Account:
    def __init__(self):
        self.acct_name = input("Enter Account Name: ")
        self.acct_number = int(input("Enter Account Number: "))
        self.balance = int(input("Enter the Balance: "))

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            print("You cannot withdraw more than you have.")
        else:
            self.balance -= amount
        self.showbalance()

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        self.balance += amount
        self.showbalance()

    def showbalance(self):
        print("Balance:", self.balance)


l=[]
while(1):
    print("1.create an account")
    print("2.withdraw")
    print("3.deposit")
    print("4.showbalance")
    print("5.exit")
    ch = int(input("Enter your choice:"))
    if ch==1:
        a=Account()
        print(a)
        l.append(a)
        print(l)
    elif ch==2:
        number=int(input("enter account number"))
        for i in l:
            if i.acct_number==number:
                i.withdraw()
                break
            else:
                print("account does not exist")
    elif ch==3:
        number=int(input("enter account number"))
        for i in l:
            if i.acct_number==number:
                i.deposit()
                break
            else:
                print("account does not exist")
    elif ch==4:
            number=int(input("enter account number"))
            for i in l:
                if i.acct_number==number:
                    i.showbalance()
                    break
                else:
                    print("account does not exist")






