#value acclocation
a=10
b=20
c=30
#reassigning the values a=c,b=a,c=a
#solution 1
a,b,c=c,a,b
print(a,b,c)
#solution 2
sum=a+b+c
a,b,c=(sum)-(a+b),(sum)-(c+a),(sum)-(a+b)
print(a,b,c)

