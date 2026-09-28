# class Parent:
#     def M1(self):
#         print("In parent class method m1")
#     def M2(self):
#         print("In parent class method m2")
# class Child(Parent):
#         def M3(self):#own attribute possible
#             print("In child class method m3")
#         def M1(self):
#             # method overding here child class o/p will come
#             super().M1()#used to completely mpdify /extend parent functionality
#             print("In child class method m1")
# c=Child()
# c.M1()
# c.M2()
# c.M3()
#
# class Person:
#     def __init__(self):
#         self.name = input("Enter your name: ")
#         self.age = input("Enter your age: ")
#
#     def show(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno = input("Enter your roll no: ")
#         self.mark = input("Enter your mark: ")
#
#     def show(self):
#         super().show()
#         print("Roll No:", self.rollno)
#         print("Mark:", self.mark)
#
#     def update(self):
#         self.mark = input("Enter new mark: ")
#         print("Mark updated successfully")
#
#
# # Object creation
# s = Student()
#
# print("\nStudent Details")
# s.show()
#
# print("\nUpdate Mark")
# s.update()
#
# print("\nUpdated Student Details")
# s.show()
# class Category:
#     def __init__(self):
#         self.category_name = input("Enter category: ")
#
#     def show_Category(self):
#         print("Category:", self.category_name)
#
#
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.product_name = input("Enter product name: ")
#         self.product_price = float(input("Enter product price: "))
#         self.quantity = int(input("Enter quantity: "))
#
#     def total_price(self):
#         print("Product:", self.product_name)
#         print("Total Price:", self.product_price * self.quantity)
#
#
# p = Product()
# p.show_Category()
# p.total_price()
class Company:
    def __init__(self):
        self.company_name = input("Enter company name: ")
        self.location = input("Enter location: ")

    def display_company(self):
        print("Company:", self.company_name)
        print("Location:", self.location)


class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empid = input("Enter Employee ID: ")
        self.empname = input("Enter Employee Name: ")
        self.salary = float(input("Enter Salary: "))

    def update_salary(self):
        self.salary = self.salary + (self.salary * 10 / 100)

    def display_details(self):#super().display_company()
        print("Employee ID:", self.empid)
        print("Employee Name:", self.empname)
        print("Salary:", self.salary)


e = Employee()
e.update_salary()
e.display_company()
e.display_details()


