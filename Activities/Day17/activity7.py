import string

def password_strength(password):
    if len(password) < 8:
        return "Weak"

    count= 0
    if any(char.islower() for char in password):
        count += 1
    if any(char.isupper() for char in password):
        count += 1

    if any(char.isdigit() for char in password):
        count += 1
    if any(not char.isalnum() for char in password):
        count += 1  
    if count <= 2:
        return "Weak"
    elif count == 3 or count == 4:
        return "Moderate"
    else:
        return "Strong"


user_password = "P@ssw0rd123"
print("Password strength:", password_strength(user_password))
