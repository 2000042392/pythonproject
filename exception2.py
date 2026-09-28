# from importlib.metadata import pass_none
# try:
#     n1 = int(input("Enter a number: "))
#     n2 = int(input("Enter another number: "))
#
#     r = n1 / n2
#     print(r)
#
# except ValueError as e:
#     print(e)
#     print(type(e))
#
# except ZeroDivisionError as s:
#     print(s)
#
# except Exception as e:
#     print(e)
#
# else:
#     pass
#
# finally:
# class MyException(Exception):
#     pass
# try:
#     n = int(input("Enter a number: "))
#
#     if n < 18:
#         raise MYException("Not eligible")
#     else:
#         print("Eligible")
# #
# # except MYException as e:
# #     print(e)
# 1. Number must be Positive (ValueError)
#
# Question: Ask the user to enter a number. If the number is less than or equal to 0, raise a ValueError with the message "Number must be Positive".
# try:
#     n=int(input("enter a number"))
#     if n<=0:
#         raise ValueError("Number must be positive")
#     else:
#         print("valid number")
# except ValueError as e:
#     print(e)
# class InvalidPasswordError(Exception):
#     pass
#
# try:
#     password = input("Enter a password: ")
#
#     if len(password) < 8:
#         raise InvalidPasswordError("Password should have 8 characters")
#     else:
#         print("Password is valid")
#
# except InvalidPasswordError as e:
#     print(e)
class InsufficientBalanceError(Exception):
    pass

balance = 5000

try:
    amount = int(input("Enter Amount: "))

    if amount > balance:
        raise InsufficientBalanceError("Not Enough Balance. Transaction Failed")
    else:
        balance -= amount
        print("Transaction Successful")
        print("Remaining Balance:", balance)

except InsufficientBalanceError as e:
    print(e)