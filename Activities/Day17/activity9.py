def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    total = 0

    for digit in num_str:
        total += int(digit) ** num_digits

    if total == n:
        return True
    else:
        return False
print(is_armstrong(153))  
