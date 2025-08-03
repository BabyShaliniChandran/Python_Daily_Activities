import string

def password_strength(password):
    # First, check if the password is long enough
    if len(password) < 8:
        return "Weak"

    count= 0

    # Check for lowercase letters
    if any(char.islower() for char in password):
        count += 1

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        count += 1

    # Check for numbers
    if any(char.isdigit() for char in password):
        count += 1

    # Check for special characters
    for symbol in string.punctuation:
        if symbol in password:
            count += 1
            break  # No need to check further once we find one

    # Decide the strength based on how many types are used
    if count <= 2:
        return "Weak"
    elif count == 3 or count == 4:
        return "Moderate"
    else:
        return "Strong"


user_password = "P@ssw0rd123"
print("Password strength:", password_strength(user_password))
