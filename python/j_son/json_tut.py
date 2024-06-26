import json
# jsonString ='{"name":"vinay","age":21}'

# pObject = json.loads(jsonString)

# # print(type(pObject))

# with open('j.txt','r') as file:
#     dic = json.load(file)

# print(dic)

dic = {'name':'om','age':'teenage'}

jString= json.dumps(dic,indent=3,separators=(',','='))

print(jString)
# with open('dump_ex.txt','w') as file:
#     json.dump(dic,file,separators=('|','->'))


