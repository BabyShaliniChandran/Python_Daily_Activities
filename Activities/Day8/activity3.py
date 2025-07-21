'''student={
"Anita":{"Math":95,"science":89},
"Ravi":{"Math":80,"science":92},
"Pavi":{"Math":85,"science":85}}
name=input("enter the name:")
print(student.get(name,"Invalid input"))
print(student.get(name.get(subject,"Invalid input")))


subject=input("enter the Subject:")
#print(student[name].get(subject,"Invalid input"))
print(student.get(name.get(subject)))

	'''


student={
"Anita":{"Math":95,"science":89},
"Ravi":{"Math":80,"science":92},
"Pavi":{"Math":85,"science":85}}
name=input("enter the name:")
subject=input("enter the Subject:")
print(student[name].get(subject,"Invalid input"))