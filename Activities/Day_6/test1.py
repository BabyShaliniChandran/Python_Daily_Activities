#input
numbers=[10,20,30,40,50,60,70,80,90,100]
#lsit to store extract ele
extract=[]
extract=extract+(numbers[1::3])
answer=extract[::-1]+(numbers[0::2])
print(answer*2)
