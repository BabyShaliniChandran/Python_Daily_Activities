def division():
	numerator=int(input("Enter numerator: "))
	while True:
		try:
			denominator=int(input("Enter denominator: "))
			result=numerator/denominator
			print(f'Result: {result}')
			break
				
		except ZeroDivisionError:
			print("Connect divide by zero!")
division()	