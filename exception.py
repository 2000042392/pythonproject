# try:
#  n1=int(input("enter first number"))
#  n2=int(input("enter second number"))
#
#  r=n1/n2
# except ValueError:
#  print("valuerror")
#
#
# except :
#  print("zero division error")
#
# else:
#  print("the result is ",r)
# finally:
#  print("done")
#  try:
#      from math import factorial
#      n=int(input("enter a number"))
#      f=factorial(n)
#      print("factorial of ",n," is ",f)
#  except ValueError:
#   print("value error")
# #
# try:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#
#     print("\nChoose Operation")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#
#     choice = int(input("Enter your choice (1-4): "))
#
#     if choice == 1:
#         print("Result =", num1 + num2)
#
#     elif choice == 2:
#         print("Result =", num1 - num2)
#
#     elif choice == 3:
#         print("Result =", num1 * num2)
#
#     elif choice == 4:
#         try:
#             print("Result =", num1 / num2)
#         except ZeroDivisionError:
#             print("Error: Division by zero is not allowed.")
#
#     else:
#         print("Invalid choice. Please select between 1 and 4.")
#
# except ValueError:
#     print("Error: Please enter valid numeric input.")
# try:
#     filename=input("enter the file name")
#     f=open(filename,'r')
#     s=f.read()
#     print(s)
#     f.close()
# except FileNotFoundError:
#     print("file not found")
# d={"name":"arun","age":23,"place":"ekm"}
# try:
#     key=input("enter your key")
#     print(d[key])
# except KeyError:
#     print("key is not exist")
# from math import factorial
#
# while True:
#     from math import factorial
#
# while True:
#     try:
#         n = int(input("Enter a number: "))
#         print("Factorial of", n, "is", factorial(n))
#         break
#     except ValueError:
#         print("Invalid input! Please enter a valid integer.")
# def fact():
#      try:
#           n=int(input("enter a number"))
#           f=math.factorial(n)
#           print(f)
#      except:
#           print("value error")#recursion a function call itself
#           fact()
#      else:
#           pass
# fact()
import math

def fact():
    while True:
        try:
            n = int(input("Enter a number: "))
            f = math.factorial(n)
            print(f)
            break          # Exit the loop after valid input
        except ValueError:
            print("Value Error! Enter a valid integer.")

fact()





