d={'a':1,'b':2}
keys=d.keys()
d['c']=3
print(len(keys))
print(d.items())
print(type(d['a']))
#d.pop()
print(d)
#to check the item is in the dict
print('x' in d)
#to check the key 
print('x' in d.keys())
#to check the values
print('x' in d.values())
#check the exact string is present in dict 
fruit_price={
"elppa":100,
"ybab":20,
"ananab":30}
print('elppa' in fruit_price)

list=[{'a':1,'b':2},{'c':3}]
print(list)

student={
"amit":{"math":97,"science":89},
"ravi":{"math":90,"science":45}
}
print(student["ravi"]["science"])

print(len(student))

