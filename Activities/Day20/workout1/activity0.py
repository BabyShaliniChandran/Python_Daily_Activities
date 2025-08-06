
try:
	import zipfile
	import os 
	folder_name=input("enter the folder path")
	file_name = os.path.basename(folder_name)
	print(file_name)
	zip_file=input("enter the zipfile")
	with zipfile.ZipFile(zip_file,mode='r') as zf:
		print(zf.namelist())
		file_name=input("choose the file which have to extract ")
		print(zf.extract(file_name))


except Exception as e:
	print(e)
