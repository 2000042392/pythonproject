# 1.Create a class named Movie with attributes moviename,year,language,director,rating
# and methods display_details() and update_rating()



# 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
#
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# # Create objects of both classes, accept input from the user, and display the details.
# class Movie:
#     def __init__(self):
#         self.moviename=input("enter  movie name")
#         self.year=int(input("enter  year"))
#         self.language=input("enter  language")
#         self.director=input("enter director name")
#         self.rating = int(input("enter  rating"))
#     def dispaly_details(self):
#         print("movie name is",self.moviename)
#         print("movie year is",self.year)
#         print("movie language is",self.language)
#         print("director is",self.director)
#         print("rating is",self.rating)
#     def update_rating(self):
#         self.rating=int(input("enter new rating"))
#         print("new rating",self.rating)
# m=Movie()
# m.dispaly_details()
# m.update_rating()
# m.dispaly_details()
class Vehicle:
    def __init__(self):
        self.brand = input("Enter brand: ")
        self.model = input("Enter model: ")
        self.color = input("Enter color: ")
        self.year = int(input("Enter year: "))

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Color:", self.color)
        print("Year:", self.year)


# class Car(Vehicle):
#     def __init__(self):
#         Vehicle.__init__(self)
#         self.mileage = int(input("Enter mileage: "))
#
#     def display(self):
#         print("\nCar Details")
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Color:", self.color)
#         print("Year:", self.year)
#         print("Mileage:", self.mileage)
#
#
# class Bike(Vehicle):
#     def __init__(self):
#         Vehicle.__init__(self)
#         self.cc = int(input("Enter CC: "))
#
#     def display(self):
#         print("\nBike Details")
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Color:", self.color)
#         print("Year:", self.year)
#         print("CC:", self.cc)
#
#
# print("Enter Car Details")
# car = Car()
# car.display()
#
# print("\nEnter Bike Details")
# bike = Bike()
# bike.display()