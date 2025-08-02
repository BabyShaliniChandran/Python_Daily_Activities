scores={
	"science":(90,80,98,88),
	"maths":(78,88,90,45),
	"English":(78,84,91,45),
	"Tamil":(69,90,74,89)
	}
def average():
	"""creating the ojects which stores the mean values of the subject"""
	for subject,marks in scores.items():
		mean=sum(marks)//len(marks)
		yield subject,mean
	
for subject,mean in average():
	print(f'{subject}:{mean}')	