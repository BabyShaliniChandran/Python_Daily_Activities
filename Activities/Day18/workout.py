'''set={range(1,100)}
print(set.pop())

multiply=lambda x,y: x*y

print(multiply(3,4) is 12)

f=lambda x:x+2,x*2
print(f(3))

my_list=(1,2,3,4,5)
result=list(map(lambda x:x**2,my_list))
print(result)

my_list=(1,2,3,4,5,6,7,8,9,10)
result=list(filter(lambda x:x%2==0,my_list))
print(result)


from functools import reduce
my_list=(1,2,3,4,5)
result=reduce(lambda x,y:x*y,my_list)
print(result)


my_list=(1,2,3,4,5,6,7,8,9,10)
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
result=list(filter(lambda x:prime(x),my_list))
print(result)




list=[x+x for x in range(10)]
print(list)


odd_squares=[x*x for x in range(11) if x%2!=0]
print(odd_squares)


prime_num = [num for num in range(11) if num>2 and any(num%x!=0 for x in range(1,int(num**0.5)+1))]
print(prime_num)


labels=[f'{x}:even' if x%2==0 else f'{x}:odd' for x in range(1,8)]

print(labels)

pairs=[(x,y) for y in range(2) for x in range (3)]
print(pairs)


import math
squares={x:math.sqrt(x) for x in range(11) if x%2!=0}
print(squares)


list=['one','two','three']
print({k:v for (k,v) in enumerate(list,start=1)})


coord={(x,y,z):x*y*z for x in range(2) for y in range(2) for z in range(2)}
print(coord)



square=lambda x:x**2
cube=lambda x:x*x*x
my_list=(1,2,3,4,5)
result=list(map(lambda x:square if x%2==0 else cube))
print(result)
'''
try:
	v1=int(input("enter the integer:"))
except ValueError:
	v1=int(input('''already entered input is worng ,
kindly enter the input:'''))

print(v1)






















