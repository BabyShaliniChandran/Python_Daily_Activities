'''
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

s={'x':10}
key_view=s.values()
s['y']=20
print(list(key_view))


s={'x':10}
s['b']=5
s['b']+=5
s['c']=4
s.popitem()
print(s)
s={'x':10}
s['b']=5
s['b']+=5
s['c']=4
s.pop('d',-1)

'''

d=({'a':5},)
v=d*2
v[0]['a']+=10
v[1]['total']=25
print(v[0]['a'],v[1]['total'])


base={'user':{'profile':{'name':'jon'}}}
update_data={'user':{'profile':{'age':25},'settingd':{'theme':'dark'}}}
base['user'].update(update_data['user'])
print(base['user']['profile'])#age:25








