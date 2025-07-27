'''
a=[[0]*2]*3
a[0][0]=99
print(a)

a=[1,2,3,4]
b=a
a+=[5]
print(b)

access_data={
(103,209):"Alice",
(104,210):"Bob",
(105,211):"Charlie",
(106,212):"Diana"
}
auth_input=input("enter the name:")
print(access_data.get(dict(zip(access_data.values(), access_data.keys())).get(auth_input.keys()), "not found"))

#set unhashable types are :list,dict,set
#bool is accepted only if the(o'

set={1,2.0,"hello",3 + 4j,False,None,(2,3)}
print(set)

word=set("programming,programming")
print(word)
print(len(word))


fruit={'apple','banana'}
fruit.add('orange')
print(fruit)

fruit.update({'apple':1},(244,4))
fruit.update('grape')
print(fruit)


s=set(["banana"])
print(s)
print(len(s))
s={1,2,3}


s={'a','b'}
s.update('cd',['e','f'])
print(sorted(s))

s=set()
print(s.pop())


s={1,2,3}
s.discard(4)
s.remove(4)
print(s)

s={'x','y','z'}
s.discard('a')
print(len(s))

a=set()
a.update([1],(2,),{3})
print(a)
print(len(a))


a={1,2}
b=a
a.clear()
print(b)

'''
num1 = 14#1110
num2= 10#1010
print (num1 & num2)
print(num1 and num2)
'''
14=1110
10=1010
--------
   1010
--------
'''

























