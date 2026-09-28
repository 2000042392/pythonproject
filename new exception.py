# 7. Factorial using Recursion
#
# Question: Use recursion to repeat input after invalid data
# import math
#
# while True:
#     try:
#         n = int(input("Enter a number: "))
#         fact = math.factorial(n)
#         print("Factorial =", fact)
#         break
#     except ValueError:
#         print("Enter a valid integer")
# import math
#
# def factorial():
#
#     try:
#         n=int(input("enter the number"))
#         factorial=math.factorial(n)
#         print(factorial)
#     except ValueError:
#         print("enter a valid number")
# factorial()
# d = {"name": "Arun", "age": 23, "place": "EKM"}
# try:
#     key=input("enter your key")
#     print(d[key])
# except KeyError:
#     print("key is invalid")
# class MyException(Exception):
#     pass
#     try:
#         age=int(input("enter your age"))
#         if age<18:
#             raise MyException("not enough age")
#         else:
#             print("eligible")
#         except MyException as e:
#                 print(e)
# 11. Custom Exception – Password Validation
#
# Question: Raise a custom exception if the password has fewer than 8 character
# class MyException(Exception):
#     pass
# try:
#     password=input("Enter your password: ")
#     if len(password)<8:
#         raise MyException("password is too short")
#     else:
#         print("password is ok")
# except MyException as e:
#     print(e)









