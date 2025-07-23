
'''
#solution 1
#user_input=input()
#print(fruit_price[user_input[::-1]])
#solution2
#print(fruit_price[input()[::-1]])

#solution 2
#sorted the keys in aplha
keys=list(fruit_price.keys())
sorted_keys=list(map(sorted,keys))

#find the index of the key
index=sorted(user_input) in sorted(sorted_keys) and sorted_keys.index(sorted(user_input))

#use the index to get the key from the dict
index_keys=keys[index]

#using index getting the values
price=fruit_price[index_keys]



user_input=input()
keys=list(fruit_price.keys())
sorted_keys=list(map(sorted,keys))
print(fruit_price[keys[sorted(user_input) in sorted(sorted_keys) and sorted_keys.index(sorted(user_input))]])




user_input=" ".join(sorted(input("enter the fruit")))

fruit_price.update(
    "".join(sorted("elppa")): {"org": "elppa", "values": fruit_price["elppa"]},
    "".join(sorted("ananab")): {"org": "ananab", "values": fruit_price["ananab"]},
    "".join(sorted("egnaro")): {"org": "egnaro", "values": fruit_price["egnaro"]}
)
 
print(fruit_price[user_input]["value"])

#declration 
fruit_price={
"elppa":100,
"ananab":20,
"egnaro":30}
sorted_keys = list(map(''.join, map(sorted, fruit_price.keys())))
print(fruit_price.get(dict(zip(sorted_keys, fruit_price.keys())).get(''.join(sorted(input("enter the fruit:"))))),"not found")
'''
 
fruit_price = {
    "elppa": 100,
    "ananab": 20,
    "egnaro": 30
}

sorted_keys = list(map(''.join, map(sorted, fruit_price.keys())))
print(fruit_price.get(dict(zip(sorted_keys, fruit_price.keys())).get(''.join(sorted(input("Enter the fruit: ")))), "not found"))







