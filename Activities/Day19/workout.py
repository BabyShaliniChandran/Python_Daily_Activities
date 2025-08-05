'''
import datetime import time 
print(datetime.datetime.now())

  
from datetime import time 

t= time(10,45,30)
print(t)
print(t.hour,t.minute,t.second)

t= time(24,45,30)
print(t)
print(t.hour,t.minute,t.second)

#date+time
from datetime import  datetime
now=datetime.now()
print(now)

print(now.year,now.month,now.day)


dt=datetime (2025,8,5,13,12)

print(f'{dt.day}-{dt.month}-{dt.year} {dt.hour}:{dt.minute}')

 '''
try:
	file_handle=open('hello.txt','r')
	content= file_handle.read()
	print(content)    
	file_handle.close()
except Exception as e:
   	print(e)


