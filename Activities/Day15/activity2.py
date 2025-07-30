#solution1
'''
sentence=input("enter the sentence:")
count=0
for char in sentence:
	if char.lower() in ['a','e','i','o','u']:
		count+=1

print("Count of the vowels:",count)
'''
#solution2

sentence=input("enter the sentence:").lower()
count=0
vowel={'a','e','i','o','u'}
for char in sentence:
	if char in vowel:
		count+=1

print("Count of the vowels:",count)


'''
sentence=input("enter the sentence:").lower()

vowel={'a','e','i','o','u'}
count = sum(char in vowels for char in sentence)
print(count)