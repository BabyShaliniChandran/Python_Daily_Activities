number=int(input("enter the number:"))
list_numbers=[1,2,3,4,5]
not_found=1
for  i in range(len(list_numbers)):
	if list_numbers[i]==number:
		print(i)
		not_found=0
if not_found:
	print("not found")
		
