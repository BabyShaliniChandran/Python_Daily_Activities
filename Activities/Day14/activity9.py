number=input("Enter the 4-digit number:")
if int(number[0])+int(number[1]) == int(number[-2])+int(number[-1]):
	print("Lucky")
else:
	print("Unlucky")
