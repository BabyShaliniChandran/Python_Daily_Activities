dict1={'x':10,'y':20}
dict2={'y':99,'z':30}
dict=dict1.update(dict2)
print(dict) 

#or 

merge={**dict1,**dict2}
print(merge)

#or 

dict=dict1|dict2
print(dict) 