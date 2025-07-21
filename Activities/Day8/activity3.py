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

#declaration
student={
"Anita":{"Math":95,"science":89},
"Ravi":{"Math":80,"science":92},
"Pavi":{"Math":85,"science":85}}
#getting the user input
name=input("enter the name:")
subject=input("enter the Subject:")
#using sclicing to get the output
print(student[name].get(subject,"Invalid input"))

