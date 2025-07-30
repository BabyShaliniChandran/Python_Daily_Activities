n_rows=int(input("enter the n rows:"))

for i in range(1,n_rows+1):
	print(' '*(n_rows-i)+'*'*((i*2)-1))

'''
#invert of the triangle
for i in range(n_rows+1,0,-1):
	print(' '*(n_rows-i)+'*'*((i*2)-1))

     *
    ***
   *****
  *******
 *********
 *********
  *******
   *****
    ***
     *
'''
