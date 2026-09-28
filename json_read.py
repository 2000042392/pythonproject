# import json
# f=open("data.json","r")
# content=json.load(f)
# print(content[0]['name'],content[0]['age'])
# print(content[1]['name'],content[1]['age'])
# f.close()
#write
import json
content=[
    {"title":"book1","author":"john","price":200},
    {"title":"book2","author":"sam","price":300}
]
f=open("books.json","w")
json.dump(content,f)
f.close()