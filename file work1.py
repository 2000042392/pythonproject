# f=open("k.txt","r")
# s=f.readlines()
# print(len(s)) #numbeer of lines in file
# f=open("k.txt","r")
# s=f.read()
# print(s.split())
# print(len(s.split()))# number of words andlength
# f=open("k.txt","r")
# s=f.readlines()
# s[1]="java"
# f.close()
# f=open("k.txt","w")
# f.writelines(s)
# f.close() update the content in second line in file
# f=open("k.txt","r")
# s=f.readlines()
# print(s[-5:]) last 5 lines
# f=open("k.txt","r")
# s=f.read()
# f.close()
# word=input("enter the word").strip()
# if word in s:
#     print("the word  found")
# else:
#     print("the word not found")
# f=open("k.txt","r")
# s=f.read()
# digit=0
# letter=0
# space=0
# for i in s:
#     if i.isdigit():
#         digit+=1
#     elif i.isalpha():
#         letter+=1
#     elif i==" ":
#       space+=1
# print("Digit",digit)
# print("Letter",letter)
# print("Space",space)
# f.close() count digits and letters
# f=open("k.txt","r")
# s=f.readlines()
# print(s[::-1])
# f.close()
# f=open("k,txt","w")
# f.writelines(s)
# f.close()

f=open("total.txt","r")
g=open("passed.txt","r")
s1=f.readlines()
print(s1)
s2=g.readlines()
print(s2)
h=open("failed.txt","w")
for i in s1:
    if i not in s2:
        h.write(i)
        f.close()
        g.close()











