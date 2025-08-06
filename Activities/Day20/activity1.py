try:
	import zipfile
	with zipfile.ZipFile(zip_file,mode='r') as zf:
		files=zf.namelist()
	if foo.txt in files:
		print("Found!")
	else:
		print("Missing!")
except Exception as e:
	print(e)
