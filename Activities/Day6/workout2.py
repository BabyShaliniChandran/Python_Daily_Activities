'''tuple=(10,20,30,40,50,60,30)
tuple_list=list(tuple)
answer=[]
answer.append(tuple_list.index(tuple_list[:2]+tuple_list[2:4]+tuple_list[:2])
print(answer)'''

'''
tuple1=(10,20,30,40,50,60)
tuple=list(tuple1)
t1=tuple.pop()
tuple.pop()
tuple1.append(t1)'''


'''
tuple1=tuple(map(int,input('enter the input').split()))
print(len(tuple1)-1)

print(tuple1.index(tuple1[-1]))
'''
'''
typle2=(10,20,30,(2,10,(-1,20,30)))
print(min(tuple2))'''

'''
tuple3 = (15, 22, 5, 10)
print(tuple3.index(min(tuple3))-1 > tuple3.index(min(tuple3)))

x=(90,101,42,67)
print(min(x+(10,)))

t=tuple(map(int,input().split()))
print(sum(t)//len(t))'''

t=(10,20,30)
del t
print(t)
'''
#update the balance
acount_info=('name','accco_no','pan_card',300,'credict,debt')
balance=acount_info[3]-200
acount_info.replace(acount_info[3],balance)
print(acount_info)

