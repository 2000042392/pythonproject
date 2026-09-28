#append
# f=open("k.txt","a")
# f.write("python")
# f.close()
#write a program to append the contents from one file into another text file
# f=open("file2.txt","r")
# s=f.read()
# print(s)
# f.close()
# f=open("file1.txt","a")
# f.write(s)
# f.close()
# f=open("k.txt","a+")
# print(f.tell())
# f.write("python")
# print(f.tell())
# f.seek(0)
# print(f.tell())
# s=f.read()
# print(s)
import os
os.remove("k.txt")
print("file is deleted")

