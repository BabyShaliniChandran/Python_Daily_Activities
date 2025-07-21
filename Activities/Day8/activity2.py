#print the middle elemenets
#solution 1
print(list(map(str,input().split()))[1:4])
#solution 2
sentence="Python makes you think diffrently".split()
first,*middle,last=sentence
print(middle)