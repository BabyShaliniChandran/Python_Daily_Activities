class TV:
	def power_on(self):
		print("Tv is now on")
class AirConditioner:
	def power_on(self):
		print("Air Conditioner is now on")
class Speaker:
	def power_on(self):
		print("Speaker is now on")
def remote_control(devide):
	device.power_on()
tv=TV()
ac=AirConditioner()
speaker=Speaker()
print(id(tv))
print(id(ac))
print(id(speaker))