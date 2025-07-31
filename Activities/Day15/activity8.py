name=["Alice","Bob","Charlies"]
marks=[85,90,88]
grades=["B","A","A"]

if len(name)==len(marks)==len(grades):
	for i in range(0,len(name)):
		print(f'{i+1},{name[i]},{marks[i]},{grades[i]}')


