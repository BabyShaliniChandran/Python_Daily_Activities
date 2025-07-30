'''
student_score=int(input("enter the score:"))

if student_score>= 90:
	Grade='A'
	print("Excellent work!")
elif student_score>=80 :
	Grade='B'
	print("Good job!")
elif student_score>=70 :
	Grade='C'
	print("satisfactory")
elif student_score>=60 :
	Grade='D'
	print("Need improvement")
else:
	Grade='F'
	print("Please study more")
print("Grade:",Grade)



grade_dict = {
    90: ('A', "Excellent work!"),
    80: ('B', "Good job!"),
    70: ('C', "Satisfactory"),
    60: ('D', "Need improvement")
}
'''


student_score = int(input("Enter the score: "))

# Dictionary mapping specific scores to grades and messages
grade_dict = {
    90: ('A', "Excellent work!"),
    80: ('B', "Good job!"),
    70: ('C', "Satisfactory"),
    60: ('D', "Need improvement")
}

# Default grade and message
default = ('F', "Please study more")

# Get grade and message from dictionary or use default
grade, message = grade_dict.get(student_score, default)

print(message)
print("Grade:", grade)

