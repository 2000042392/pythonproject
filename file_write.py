# #write operation
# f=open('k.txt','w')#if file exist it will erase the file contents and returns# its reference to f else it will create a new empty file and returns its reference to f
# #f.write(string)
# #f.writelines(lists)
# f.write("hello\n")
# f.close()
# f = open("k.txt", "w")
# f.write("hello\n")
# f.close()
#
# print("File created successfully")
# f = open("k.txt", "w")
#
# f.writelines(['hello\n','kittu\n'])
# f.close()
f=open("k.txt",'w')
f.writelines(s)

