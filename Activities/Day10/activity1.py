'''students={'Alice','Bob','Charlies'}
new_entries=['Charlies','Diana','Eve','Bob','Frank']
len_old_student_name=len(students)
students.update(new_entries)
print("the count of new entries:",(len(students)-len_old_student_name))
'''

from collections import Counter

students={'Alice','Bob','Charlies'}
new_entries=['Charlies','Diana','Eve','Bob','Frank']

new_entries+=students
count=(Counter(new_entries))
student_list=set(count.items())
print(student_list)

