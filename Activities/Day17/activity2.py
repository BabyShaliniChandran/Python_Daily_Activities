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
'''
n=100

output=list(range(2,n+1))

def numbers(divisor_number):
	divisor=divisor_number
	result=[]
	for num in output:
		if num==divisor:
			result.append(num)
		if num%divisor!=0:
			result.append(num)	
	return result


for i in range(2,(n+1)//2):
	output=numbers(i)
	print(numbers(i))

