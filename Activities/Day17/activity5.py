#fibonacci 0,1,1,2,3,5
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib=fibonacci()
while True:
	print(next(fib))
