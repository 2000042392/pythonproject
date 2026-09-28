# from abc import ABC, abstractmethod
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
#
# class Rectangle(Shape):
#
#     def __init__(self):
#         self.length = int(input("Enter the length of the rectangle: "))
#         self.breadth = int(input("Enter the breadth of the rectangle: "))
#
#     def get_area(self):
#         print("Area:", self.length * self.breadth)
#
#     def get_perimeter(self):
#         print("Perimeter:", 2 * (self.length + self.breadth))
#
#
# r = Rectangle()
# r.get_area()
# r.get_perimeter()
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
#
# class Square(Shape):
#
#     def __init__(self):
#         self.side = int(input("Enter the side of the square: "))
#
#     def get_area(self):
#         print("Area:", self.side * self.side)
#
#     def get_perimeter(self):
#         print("Perimeter:", 4 * self.side)
#
#
# s = Square()
# s.get_area()
# s.get_perimeter()
from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self):
        self.name = input("Enter employee name: ")

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self):
        super().__init__()
        self.salary = int(input("Enter salary: "))

    def calculate_salary(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


class PartTimeEmployee(Employee):

    def __init__(self):
        super().__init__()
        self.rate = int(input("Enter rate: "))
        self.hours = int(input("Enter the hours: "))

    def calculate_salary(self):
        print("Employee Name:", self.name)
        print("Salary:", self.rate * self.hours)


f = FullTimeEmployee()
f.calculate_salary()

p = PartTimeEmployee()
p.calculate_salary()
