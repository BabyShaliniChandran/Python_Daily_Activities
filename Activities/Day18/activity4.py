data=[('Charlies',90),('Alice',90),('Bob',75),('Dave',60)]
sorted_key = lambda x:(-x[1],x[0])
result=sorted(data,key=sorted_key)


print(result)		
		
