a,b,c=(map(str,input("enter the string ").split(",")))
set_string=set([a,b,c])
if  all([a,b,c]) and len(set_string)==3:
	print("All unique and non-empty element")

