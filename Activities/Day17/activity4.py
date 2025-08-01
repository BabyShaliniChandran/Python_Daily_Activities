username="@babyshalini"
first_name="baby"
last_name="priya"
password="Password123"

def password_has_lower():
    return any(char.islower() for char in password)


def password_has_upper():
    return any(char.isupper() for char in password)


print(password_has_lower())
print(password_has_upper())
def password_validation():
	if (username!=password and 
	    password not in first_name and 
	    password not in last_name and 
	    len(password)>=10 and 
	    password.isalnum() and 
	    password_has_lower() and 
	    password_has_upper()
	  ):
		return ("Password is valid")
	else:
		return ("not valid")
print(password_validation())


	

		