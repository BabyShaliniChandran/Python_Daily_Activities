integer=int(input("Enter the number:"))

for number in range(2,integer+1):
	is_prime=True
	for num in range(2,int(number**0.5)+1):
		if number % num ==0:
			is_prime=False
			break
	if is_prime:
		print(number)