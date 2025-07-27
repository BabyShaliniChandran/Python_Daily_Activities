dict1={'x':10,'y':(20,30)}
dict2={'z':20,'y':30}

access_data={
(103,209):"Alice",
(104,210):"Bob",
(105,211):"Alice",
(106,212):"Diana"
}

updated_dict={}
updated_dict.update(dict(zip(set(access_data.values()),access_data.keys())))
print(updated_dict)