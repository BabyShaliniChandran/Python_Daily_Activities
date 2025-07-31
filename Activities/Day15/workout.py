'''
primes=[2,3,5,7]
for number in primes:
	print(f'{number} is a prime number.')


#iterate over keys(default)
student_scores={'Alice':95,'Charlies':92,'Bob':88}
for name in student_scores:
	print(name)


#iterate over items(key-value pairs)
for name,score in student_scores.items():
	print(f'{name}:{score}')


unique_color={'red','blue','green'}
for color in unique_color:
	print(color)

numbers={7,8,1,3,2}
for num in numbers:
	prinSt(num)



for i in range(2,2):
    print(i)

print(list(zip(['a','a','a'],[1,2])))

for i in range(2):
	for j in range(3):
		if j==1:
		   continue
		print(j,end="")

'''

magic=9
user_input=int(input("enter the magic_number"))
min_window=0
max_window=100
while user_input!=magic:
	if user_input==magic:
		print("magi")
		break
	if user_input>magic:











