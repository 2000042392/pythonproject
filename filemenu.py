# #1.file read
# #2.file write
# #3.file append
# #4.file search
# #file delete
# #exit
# import os
#
# # 1. File Read
# def file_read():
#     filename = input("Enter filename: ")
#     try:
#         f = open(filename, "r")
#         s = f.read()
#         print("\nFile Content:")
#         print(s)
#         f.close()
#     except FileNotFoundError:
#         print("File not found.")
#
# # 2. File Write
# def file_write():
#     filename = input("Enter filename: ")
#     data = input("Enter text to write: ")
#     f = open(filename, "w")
#     f.write(data)
#     f.close()
#     print("Data written successfully.")
#
# # 3. File Append
# def file_append():
#     filename = input("Enter filename: ")
#     data = input("Enter text to append: ")
#     f = open(filename, "a")
#     f.write("\n" + data)
#     f.close()
#     print("Data appended successfully.")
#
# # 4. File Search
# def file_search():
#     filename = input("Enter filename: ")
#     word = input("Enter word to search: ")
#
#     try:
#         f = open(filename, "r")
#         s = f.read()
#         if word in s:
#             print("Word found.")
#         else:
#             print("Word not found.")
#         f.close()
#     except FileNotFoundError:
#         print("File not found.")
#
# # 5. File Delete
# def file_delete():
#     filename = input("Enter filename: ")
#     if os.path.exists(filename):
#         os.remove(filename)
#         print("File deleted successfully.")
#     else:
#         print("File not found.")
#
# # Menu
# while True:
#     print("\n------ Menu Driven File Operations ------")
#     print("1. File Read")
#     print("2. File Write")
#     print("3. File Append")
#     print("4. File Search")
#     print("5. File Delete")
#     print("6. Exit")
#
#     ch = int(input("Enter your choice: "))
#
#     if ch == 1:
#         file_read()
#     elif ch == 2:
#         file_write()
#     elif ch == 3:
#         file_append()
#     elif ch == 4:
#         file_search()
#     elif ch == 5:
#         file_delete()
#     elif ch == 6:
#         print("Program exited.")
#         break
#     else:
#         print("Invalid choice.")