def sum(numbers):
	"""this function returns the sum of the  elements in the list""" 
	sum=0
	for i in numbers:
		sum+=i
	return sum
numbers=list(map(int,input("enter the list of numbers sperated by comma:").split(",")))
print(sum(numbers))
	