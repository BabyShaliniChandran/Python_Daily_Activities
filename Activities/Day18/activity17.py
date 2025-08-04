number=int(input("Enter the number: "))
def check_even(number):
	if number%2==0:
		return number
	else:
		raise ValueError("Odd number")
print(check_even(number))
		