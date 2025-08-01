n=100

output=[]
for i in range(2,n+1):
	output.append(i)


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