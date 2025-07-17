#step 1 -get the username
#step 2-that input in lower case
#step 3-convert into upper case with out using .upper()

username=input("enter the username")
username=username.lower()
print(chr(ord(username)-33))

#A=65
#a=97
letter=list("hello")
output=""
output+=chr(ord(letter[0])-32)
output+=chr(ord(letter[1])-32)
output+=chr(ord(letter[2])-32)
output+=chr(ord(letter[3])-32)
output+=chr(ord(letter[4])-32)
print(output)
output1=""