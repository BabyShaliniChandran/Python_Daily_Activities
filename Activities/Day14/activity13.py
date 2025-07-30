numbers=input("enter the numbers").split(",")
if sorted(numbers)==numbers:
	print("Ascending")
elif numbers==numbers[::-1]:
	print("Descending")
else:
	print("Unordered")
