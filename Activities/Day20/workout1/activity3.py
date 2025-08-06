#create new zip file

import zipfile

for i in range(1,4):
	with open (f't{i}.txt','w') as f:
		f.write(f'hello file{i}')


with zipfile.ZipFile('activity3.zip','w',compression=zipfile.ZIP_BZIP2) as z:
	for i in range(1,4):
		z.write(f't{i}.txt')
	for i in range(1,4):
		info=z.getinfo(f't{i}.txt')
		print(f'{info.filename}->{info.compress_size}bytes')
