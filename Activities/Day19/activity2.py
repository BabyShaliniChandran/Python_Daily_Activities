import random
participants=["Michael","Jim","Pam","Dwight","Angela"]
seen=[]
index=0
while True:
	secret_santa=random.choice(participants)
	while secret_santa not in seen :
		if participants[index] != secret_santa:
			print(f'{participants[index]} => {secret_santa}')
			seen.append(secret_santa)
			index+=1
			break
	if index==len(participants):
		break
			

			

			
	

