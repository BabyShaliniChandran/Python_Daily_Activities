#activity 2
#Swap the numbers with out using 3rd variable
#solution 1
x=5
y=7
x=x+(abs(x-y))
y=y-(abs(x-y))
print(x,y)

#solution 2
x=5
y=7
sum=x+y
x=(sum)-x
y=(sum)-y
print(x,y)