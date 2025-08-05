try:
	import mymath 
	a,b=map(int,input("enter the value1,value2:").split(","))
	print(mymath.add(a,b))
	print(mymath.subtract(a,b))
	print(mymath.multiply(a,b))
	print(mymath.divide(a,b))
except Exception as e:
   	print(e)