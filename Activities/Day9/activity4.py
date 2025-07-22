dict1={"name":"Ravi","age":23}
dict2={"age":30,"city":"Chennai"}
dict=dict1|dict2
print(dict)
#or 
merge={**dict1,**dict2}
print(merge)