Booleans=input("enter three Boolean values:").split(",")
if Booleans.count("True")==1:
	print("Exactly one")
Booleans.count("True")!=1 and print("Nope")