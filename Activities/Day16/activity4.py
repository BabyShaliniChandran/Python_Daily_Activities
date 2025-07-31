import random
secret_number=random.randint(1,100) 
while True:
	user_input=int(input("enter the number:"))
	if user_input==secret_number:
		print("correct")
		break
	if user_input<secret_number:
		print("too low")
	else:
		print("too high")
		
		
	