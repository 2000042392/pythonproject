# # uestion: Write a Python program to divide two numbers using try, except, else, and finally.
# try:
#     n1=int(input("enter first number"))
#     n2=int(input("enter second number"))
#     result=n1/n2
# except ZeroDivisionError:
#     print("division by zero error")
# else:
#     print(result)
# finally:
#     print("finally statement finished")
# 2. Factorial with Exception Handling
#
# # Question: Find the factorial of a number using exception handling# .
# import math
#
# try:
#     n = int(input("Enter a number: "))
#     fact = math.factorial(n)
#
# except ValueError:
#     print("Invalid input")
#
# else:
#     print("Factorial =", fact)
#
# finally:
#     print("Done")
# 3. Simple Calculator using Exception Handling

# Question: Create a calculator with Addition, Subtraction, Multiplication, and Division
# try:
#
#     n1 = int(input("Enter a number: "))
#     n2 = int(input("Enter another number: "))
# print("addition")
# print("subtraction")
# print("multiplication")
# print("division")
# choice = int(input("Enter your choice: "))
# if choice == 1:
#     print("addition is", n1 + n2)
# elif choice == 2:
#    print("subtraction is", n1 - n2)
# elif choice == 3:
#    print("multiplication is", n1 * n2)
#  elif choice == 4:
# print("division is", n1 / n2)
# except ZeroDivisionError:
# print("zero division error")
# else:
# print("invalid choice")
# finally:
# # print("done")
# try:
#     n1 = int(input("Enter a number: "))
#     n2 = int(input("Enter another number: "))
#
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#
#     choice = int(input("Enter your choice: "))
#
#     if choice == 1:
#         print("Addition is", n1 + n2)
#
#     elif choice == 2:
#         print("Subtraction is", n1 - n2)
#
#     elif choice == 3:
#         print("Multiplication is", n1 * n2)
#
#     elif choice == 4:
#         try:
#             print("Division is", n1 / n2)
#         except ZeroDivisionError:
#             print("Zero Division Error")
#
#     else:
#         print("Invalid Choice")
#
# except ValueError:
#     print("Invalid Input")
#
# finally:
#     print("Done")
# 4. File Handling with Exception
#
# Question: Read a file and handle FileNotFoundError# .
# try:
#     filename = input("Enter filename: ")
#     f = open(filename, "r")
#     s = f.read()
#     print(s)
#     f.close()
#
# except FileNotFoundError:
#     print("File not found")
#
# else:
#     print("File found")