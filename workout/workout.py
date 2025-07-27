'''dict1={'x':10,'y':(20,30)}
dict2={'z':20,'y':30}

access_data={
(103,209):"Alice",
(104,211):"Bob",
(105,211):"Charlies",
(106,212):"Diana"
}


access={
"Alice":(103,209),
"Bob":(104,211),
"Charlies":(105,211),
"Diana":(106,212)
}

updated_dict={}
updated_dict.update(dict(zip(set(access_data.values()),access_data.keys())))
d2 = {v: k for k, v in access.items()}
print(d2)
'''
#ordered set 

from ordered_set import OrderedSet

createOrderedSet = OrderedSet(
    ['GFG', 'is', 'an', 'Excellent', 'Excellent', 'platform'])

print(createOrderedSet)
