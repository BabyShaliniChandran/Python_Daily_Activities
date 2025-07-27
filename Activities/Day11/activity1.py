lists = [[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]

result = list(set.intersection(*map(set, lists)))

print(result) 
