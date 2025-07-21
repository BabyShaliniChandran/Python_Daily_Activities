'''list_tuple=[1,2,3,(2,3,[2,3])]
list_tuple[3][2][0]=4
#print(list_tuple)

#tuple1=(2,3,4,tuple(map(int,input("enter the numbers:").split(" "))))
#print(tuple1)
v1=print()
#print(v1)
v2=tuple(type(v1,))
#print(v1,v2)
#v3=(,)
#print(v3)
#print(print())
v4=(bool(1))
print(v4)
print(type(v4))


val1=(1,2,3)
val2=type(type(val1))
print(val1,val2)

tuple=(1,2,3,4)
list=list(tuple)
print(type(list))

tuple1=(1,2,3,4,5,6,7,8,9,10)
first,*middle,last=tuple1
print(first)
print(middle)
print(last)

numbers=tuple((input("enter the value:")))
first,*middle,last=numbers
print(type(first))
print(type(middle))
print(type(last))

numbers=tuple((input("enter the value:")))
*first,=numbers
print(first)
print(type(first))
print(len(first))
print(first[0]) 

numbers=(1,2,3,4,5,6)
first,*middle,last=numbers
print(type(first))
print(type(middle))
print(type(last))
a,b=[1,2]
print(type(a))
(a,(b,c))=(1,(2,3))


from collection import nametuple
Student=namedtuple('Student',['name','age','grade','score'])
student=Student("Anita",22,"A",95)
print(student.grade)
'''

Dictionary 





