list_code=['123','Ab23','a--123','1245','0000',1234]

for code in list_code:
	if not code.isdigit():
		continue
	if code.isdigit() and int(code)+1==1:
		break
	
	print(code)

	
