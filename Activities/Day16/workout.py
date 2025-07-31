'''
def stats(x,y):
	return [x+y,x*y]
print(stats(2,5))
print(type(stats(2,5)))
v1=stats(3,10)
print(v1,type(v1))


def user_function(x):
	return max(list)

list=[2,3,1,5,7]
print(user_function(list))



def user_function(x):
	return x=5


print(user_function())

def divide(numerator,denominator):
	return numerator/denominator
print(divide(denominator=2,10))
print(divide(10,denominator=2))



def greet(name,time="morning"):
	print(f"Good{time},{name}!")
greet("Alice")
greet("Bob","evening")


def extend_list(val,lst=[]):
	lst+=[val]
	return lst
v1=(extend_list(1))
v2=(extend_list(2,[]))
v3=(extend_list(3))
v4=(extend_list(4))

print(f'v1:{(id(v1),v1)},v2:{(id(v2),v2)},v3:{(id(v3),v3)},v4:{(id(v4),v4)}')


def total(*args):
	print(args)
	return sum(args)
print(total(2,3.0,4))
print(total(10))
print(total())



def foo(*args):
	print("args:",args)
	return
print(foo(1,2,3))
'''
def show(**kwargs):
	print(kwargs)
show(age=30)

def tag(*args,**kwargs):
	print("[log]",*args,**kwargs)
tag("hello","world",sep="~",end="$$\n")

def greet(name):
	"""Greets the person by name."""
	print(f"Hello, {name}")
greet("babe")









