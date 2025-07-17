#day 2 activity
#find the greatest variable 
a=1
b=5
#solution 1
print(max(a,b))
#solution 2
if a>b:
    print(a)
else:
    print(b)
#solution 3
list=[a,b]
diff = a - b
sign = (diff >> 31) & 1
print(list[sign])
#solution 4
print(a*(a >= b)+b * (b > a))
#solution 5
print('A is greater than b is the statement:',a>b)