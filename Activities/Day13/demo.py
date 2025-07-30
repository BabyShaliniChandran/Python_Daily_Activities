'''
mark1,cutoff=map(int,input("eneter the make:").split(","))
diff=mark1-cutoff
if (~diff):
	print("pass")


mark1,cutoff=map(int,input("eneter the make:").split(","))
if (mark1%cutoff is not mark1):
	print("pass")


mark1,cutoff=map(int,input("eneter the make:").split(","))
if (mark1-cutoff):
	print("pass")




mark1,cutoff=map(int,input("eneter the make:").split(","))
if (mark1%cutoff is not mark1):
	print("pass")
#use abs 

marks, cutoff = map(int, input("Enter marks and cutoff separated by a comma: ").split(","))

if (marks - cutoff + abs(marks - cutoff)) // 2 is (marks - cutoff):
    print("Pass")


marks, cutoff = map(int, input("Enter marks and cutoff separated by a comma: ").split(","))
if (marks - cutoff + abs(marks - cutoff))//2 is (marks - cutoff):
    print("Pass")
'''

marks, cutoff = map(int, input("Enter marks and cutoff separated by a comma: ").split(","))
diff=cutoff-marks
x=diff+abs(diff)
if not x:
	print("pass")










