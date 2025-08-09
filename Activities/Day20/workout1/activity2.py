try:	
	import zipfile
	with zipfile.ZipFile('activity2.zip',mode='w') as zf:
		zf.write('text1.txt')
		zf.write('text2.txt')
		zf.write('text3.txt')
		print(zf.namelist())
	#write the text in the file 
	for i in range(1,4):
		with open(f'text{i}.txt','w') as t:
			t.write(f"Hello from file{i}!")
	
	#extracting the files from the zip
	with zipfile.ZipFile('activity2.zip',mode='w') as zf:
		zf.extractall()
	
	#reading the file 
	for i in range(1,4):
		print(open(f'text{i}.txt').read())
except Exception as e:
	print(e)

