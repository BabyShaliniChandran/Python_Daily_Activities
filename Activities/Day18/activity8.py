fruits=['apple','banana','cherry']
len_string=[len(x) for x in fruits]
print({k:v for (k,v) in zip(fruits,len_string)})