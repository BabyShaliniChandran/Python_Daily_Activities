def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_next_prime(n):
    for candidate in range(n + 1, 1001):
        if prime(candidate):
            return candidate
    return "Not found"


N = 87
result = find_next_prime(N)
print("Next prime after", N, "is:", result)
