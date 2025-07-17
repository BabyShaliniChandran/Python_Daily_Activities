#\n used to cut the string and print in next line 
print("Hello \n world")
#to print multiple items in order seprated by ","
print("sum",2+3)
#custom separators:sep
print("2025","16","07",sep="-")
#custom endings : end 
print("loading",end="/")
print("done")
#using f-string
name="Anand"
marks=95
print(f"Name: {name},\n mark: {marks}")
x=432
x=str(x)
print(x[1])
#solution 2
x=432
x=str(x)
print(x[1:2])
#multiple line input 
#x,y=input("enter the input :").split(",")
#print(x,y)
#type casting to int using map
#v1,v2=map(int,input("enter two number").split(','))
print()
#5 values get as input
#v1,v2=int(input("enter int")),float(input("enter float"))
#print(v1,v2)
#ascii
print(ord('A'))
print(chr(65))

print(chr(100))

#list
letter=list("hello")
print(letter[0].upper()+letter[1].upper()+letter[2].upper()+letter[3].upper()+letter[4].upper())
print(*list('hello'.upper()))

list1=[1,2,3,4]
print(list1)
print(*list1)
print(type(list1))
#print(type(*list1))
print(*list('hello'.upper()))

letter=list("hello")
output=""
print(*(letter[0].upper()+letter[1].upper()+letter[2].upper()+letter[3].upper()+letter[4].upper()))
a=[1,2,3]
color=['red','green']
print(color[0][0])
numbers=[123,287,9001]
output1=""
for alp in range(len(letter)):
    output1+=(chr(ord(letter[alp])-32))
print(output1)

word=["Greek","for","Geeks"]
output=[]
for alp in word:
    out=""
    for let in alp.lower():
        out+=((chr(ord(let)-32)))
    output.append(out)
print((" ".join(output)))

#print(str(numbers[3])[3])
number=[1,2,3,4,5,6,7,8]
print(number[-1:-5:-1])

a=[1,2,3]
b=[4,5]
c=a+b
print(type(c))
A=["hi","hello"]
print(A*3)
print('blue' not in 'blue')
a=[1,2,3]
b=a.copy()
b[0]=100
print(a)
print(b)
a1=[1,2,3]
b1=[9,8,4]
c1=[6,7,8]
a1.extend(b1)
print(a1)
#index
names=['alice','bob']
print(names[0].index('i'))
#insert
names.pop('bob')
print(names)