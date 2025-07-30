integer=input("enter the integer:").split(",")
if int(integer[0])&1==0 and int(integer[1])&1!=0:
	print("Exactly one is odd!")
