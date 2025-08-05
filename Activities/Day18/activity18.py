avg_score=90
students = [     {"name": "Brenda", "scores": [90, 92, 95, 88]},     {"name": "David", "scores": [85, 87, 89]},     {"name": "Cathy", "scores": [98, 99, 100]},     {"name": "Alex", "scores": [70, 100]} ]

'''
student= {sub_dict["name"]:sum(sub_dict["scores"])/len(sub_dict["scores"]) for sub_dict in students  if sum(sub_dict["scores"])/len(sub_dict["scores"])>=90}
print(student)
'''

result=list(filter(lambda stud:sum(stud["scores"])/len(stud["scores"])>=90,students))
student= {sub_dict["name"]:sum(sub_dict["scores"])/len(sub_dict["scores"]) for sub_dict in result}
print(student)