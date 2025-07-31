'''
integer=int(input("enter the input:"))
count=0
while integer>=0:
	integer-=3
	count+=1
print(count)
'''
integer=int(input("enter the input:"))
count=0
for i in range(0,(integer//3)+1):
	if integer>=0:
		integer-=3
		count+=1
print(count)


