import zipfile 
'''
with zipfile.ZipFile('achive.zip',mode='r') as zf:
	zf.read('text1.txt')
	zf.read('text2.txt')
	zf.read('text3.txt')
	print(zf.namelist())
	zf.extractall()
'''
#create new zip file
with zipfile.ZipFile('data.zip','w',compression=zipfile.ZIP_DEFLATED) as zipf:
	zipf.write('report.txt')

#replce new zip file
with zipfile.ZipFile('achive.zip','w',compression=zipfile.ZIP_DEFLATED) as zipf:
	zipf.write('report.txt')

