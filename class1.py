# class Person:
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a
#
#     def show(self):
#         print(self.name, self.age)
#
#
# p1 = Person("Arun", 23)
# p1.show()
#
# p2 = Person("Amal", 24)
# p2.show()

# class Person:
#     def __init__(self):
#         self.name = input("Enter name: ")
#         self.age = int(input("Enter age: "))
#
#     def show(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#
#
# p1 = Person()
# p1.show()
#
# p2 = Person()
# p2.show()

# class Employee:
#     def __init__(self):
#         self.empid=int(input("enter employee id"))
#         self.name=input("enter employee name")
#         self.age=int(input("enter employee age"))
#         self.salary=int(input("enter employee salary"))
#         self.designation=input("enter employee designation")
#     def getsalary(self):
#         print("salary",self.salary)
#     def showdetails(self):
#             print("employee name",self.name,"age",self.age)
#
# e = Employee()
# e.getsalary()
# e.showdetails()
# class Student:
#     def __init__(self):
#         self.name = input("Enter student name: ")
#         self.rollno = input("Enter roll no: ")
#         self.mark1 = int(input("Enter mark1: "))
#         self.mark2 = int(input("Enter mark2: "))
#         self.mark3 = int(input("Enter mark3: "))
#
#     def display(self):
#         print("Name:", self.name)
#         print("Roll No:", self.rollno)
#         print("Total Marks:", self.mark1 + self.mark2 + self.mark3)
#
# s = Student()
# s.display()
# class Book:
#     def __init__(self):
#         self.title=input("Enter Book Title: ")
#         self.author=input("Enter the author:")
#         self.price=input("Enter the price:")
#         self.pages=input("Enter the pages:")
#         self.language=input("Enter the language")
#     def gettitle(self):
#           print("title:",self.title)
#     def getauthor(self):
#             print("author:",self.author)
#     def getprice(self):
#         print("price:",self.price)
#     def settitle(self):
#         self.title=input("Enter  new Book Title: ")
#         self.gettitle()
#     def setauthor(self):
#         self.author=input("Enter  new Book Author: ")
#         self.getauthor()
#     def setprice(self):
#             self.price=input("Enter  new Book Price: ")
#             self.getprice()
# b=Book()
# b.gettitle()
# b.getauthor()
# b.getprice()
# b.settitle()
# b.setauthor()
# b.setprice()
#
# class Account:
#     def __init__(self):
#         self.acct_name = input("Enter Account Name: ")
#         self.acct_number = int(input("Enter Account Number: "))
#         self.balance = int(input("Enter the Balance: "))
#
#     def withdraw(self):
#         amount = int(input("Enter the amount to withdraw: "))
#         if amount > self.balance:
#             print("You cannot withdraw more than you have.")
#         else:
#             self.balance -= amount
#         self.showbalance()
# l=[10,20,30]
#


#
#     def deposit(self):
#         amount = int(input("Enter the amount to deposit: "))
#         self.balance += amount
#         self.showbalance()
#
#     def showbalance(self):
#         print("Balance:", self.balance)
#
#
# # Object creation
# a = Account()
#
# # Method calls
# a.deposit()
# a.withdraw()
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

# a1=Account()
# a2=Account()
# # Object creation
# # a = Account()
# #
# # # Method calls
# # a.deposit()
# # a.withdraw()
# l=[a1,a2]
# for i in l:
#     print(i.acct_name)
#     i.showbalance()








