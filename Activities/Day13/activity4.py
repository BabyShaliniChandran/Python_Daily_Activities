previous_meter_reading=int(input("Enter the previous meter reading:"))
current_meter_reading=int(input("Enter the current meter reading:"))
units=abs(previous_meter_reading-current_meter_reading)
if units>=1000:
	print("Rate:",units*11.80)
elif units>=801:
	print("Rate:",units*10.70)
elif units>=601:
	print("Rate:",units*9.65)
elif units>=501:
	print("Rate:",units*8.55)
elif units>=401:
	print("Rate:",units*6.45)
else:
	print("Rate:",units*4.80)


