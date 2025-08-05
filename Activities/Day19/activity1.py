import random
def flip_biased_coin():
	if random.random()<=0.7:
		print("Head")
	else:
		print("Tails")
flip_biased_coin()