S='abczacc'
k=3
#output:aabcd
#explanation: ab+cd+a (sort the splited string)
#output = a+ab+cd = aabcd

'''
input string= abcda
k=3
output:abcda
explanation : abc+da
output= abc+da=abcda

abk=2
ab+zc+a=aabzc



#solution
def function(S,k):
	result=[]
	for i in range(0,len(S),k):
		result.append(S[i:i+k])
	result=sorted(result)
	return ''.join(result)
print(function(S,k))

#soltion_2
def function(S,k):
    chunks = [S[i:i+k] for i in range(0, len(S), k)]
    chunks.sort(key=len)
    return ''.join(chunks)
print(function(S,k))






if b[i] > a[i]
take the credits >= |a[i]- b[i]|

output :12

explanation :|4-3| = |1-10| remaing is 9 
return the longest good number.
'''

n=12
b=[1,2,3,3,2,1,1,2,3,3,3,3]
a=[0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]
c=10
for i in range(0,n):
	if a[i] <= b[i] and c>0 and abs(a[i]-b[i])<=c:
		c-=abs(a[i]-b[i])
		index=i
print(index+1)

		
