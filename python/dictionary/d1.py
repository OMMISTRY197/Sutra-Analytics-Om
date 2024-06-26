dic2D = {'0':{'name':{'name':'om','lname':'mistry'},'marks':[1,2,6,4,5]}}

dic2D['0']['marks']
print(dic2D['0']['name'])

dic = {'name':'Om','age':17}

keys = dic.keys()
values = dic.values()
items = dic.items()
# del dic['name'] # to delete key
dic['gender']='male'# to insert new key and key name should be unique

# dic['name']= 'Arya' # update value
dic['fName'] = dic['name']#->om
del dic['name']
print(dic)

# l1 = [1,2,2,1,3,4,5,6,77,7]

# l1_set= set(l1)
# print(l1_set)
