Username="admin"
og_password="secret123"
optional_password="letmein"
username,password=map(str,input("Enter the username,paswword:").split(","))

if username == Username and (password == og_password or password==optional_password):
	print("grant access")
else:
	print("access denied")


