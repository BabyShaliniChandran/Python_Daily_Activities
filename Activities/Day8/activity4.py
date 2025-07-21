#declration 
fruit_price={
"elppa":100,
"ybab":20,
"ananab":30}
#solution 1
user_input=input()
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
print(price)


