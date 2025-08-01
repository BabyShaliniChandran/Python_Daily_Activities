'''
import math
x=10#global variable
def sum():
	x=4 #==>Local variable
	y=20
	x=math.sqrt(x)
	return x+y
print(sum())
print(x)



x="Global"
def outer():
	def inner():
		print(x)
	x="en"
	return inner
f=outer()
f()


def numbers():
    return [1, 2, 3]

print(numbers())


def numbers():
    for i in [1, 2, 3]:
        yield i

print(numbers())

for number in numbers():
    print(number)
'''


def Shalini():
	"""Shalini function"""
	return "Shalini"
print(Shalini.__doc__)








