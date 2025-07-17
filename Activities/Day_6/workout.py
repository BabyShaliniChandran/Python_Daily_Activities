#print(sum([]))
print(5+4,1,'rja',3,True,2>>1,2<<1,None,[1,'raja',2.3,None])
list=[1,2,3]
tuple=tuple(list[1:3])
print(type(tuple))

tuple1=(1,2,3,4)
tuple2=(1,'raja',2.0)
tuple3=()
tuple4=(1,2,3,(2,3,4))
nested=((1,2),(2,3),(4,5))
print(nested[1:3])


#2 nd tuple 1st index
nested=((1,2),(2,3),(4,5))
print(nested[-2][0])

tuple=(1,2,(2,3,4,(2,3,4)))
print(len(tuple))

print(tuple.index(2))
