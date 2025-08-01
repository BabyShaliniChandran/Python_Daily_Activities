n=100

output=[]
for i in range(2,n+1):
	output.append(i)
'''
def prime_numbers():
	result=[]
	for i in range(2,n+1):
		for j in output:
			if i==j:
				result.append(j)
			if (j%i!=0):
				result.append(j)
		return result
print(prime_numbers())


def numbers():
	result=[]
	for i in range(2,n+1):
		for j in output:
			if i==j:
				result.append(j)
			if (j%i!=0):
				result.append(j)
		return result
print(numbers())

n=100

list_numbers=list(range(2,n+1))

def numbers(divisor_number):
	"""return the list of number which is not divisible by the number"i" from the loop"""
	divisor=divisor_number
	result=[]
	for num in list_numbers:
		if num==divisor:
			result.append(num)
		if num%divisor!=0:
			result.append(num)	
	return result


for i in range(2,(n+1)//2):
	list_numbers=numbers(i)
	print(list_numbers)

'''

n=100

list_numbers=list(range(2,n+1))

def numbers(divisor_number):
	"""return the list of number which is not divisible by the number"i" from the loop"""
	divisor=divisor_number
	result=[]
	for num in list_numbers:
		if num==divisor:
			continue
		if num%divisor==0:
			list_numbers.remove(num)
			
	return list_numbers


for i in range(2,(n+1)//2):
	print(numbers(i))




