list=[2,3,4,5,6]
index=int(input("Enter index: "))
try:
	print(list[index])
	print("Found")
except IndexError:
	print("Out of bounds")
