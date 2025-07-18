#(number.isdigit() and print(int(number) % 3 == 0 and "jugs")) or (number=input("enter the number 0-9:" and number.isdigit() and print(int(number) % 3 == 0 and "jugs")))

#number= input("Enter the number: ")
#number.isdigit() and print(int(number) % 3 == 0 and "jugs") or (number.isalpha() and (number:= input("Enter the number in 0-9: ").isdigit() and print((int(number) % 3 == 0 and "jugs")or number)))
#num=input().isdigit() and print(int(num)%3==0 and "jujs") or int(input())
#print(num)
#ip = int(input("Enter the number: ").isdigit()  or input("Kindly enter numeric value: "))


'''num =int((number := input("Enter the number: ")).isdigit() or (number := input("Kindly enter numeric value: ")))
print((num%3==0 and "jugs") or num)'''

#numb=int(number := input("Enter the number: ")).isdigit() and number or (input("Kindly enter numeric value: "))
#print((numb % 3 == 0 and "jugs")or numb)


'''33=jujs jujs
numb=(number := input("Enter the number: ")).isdigit() and number or (input("Kindly enter numeric value: "))
print(int(numb[0]))
print(((int(numb[0]) % 3 == 0 and "jugs")or numb[0]),end="") 
print(((int(numb[1]) % 3 == 0 and "jugs")or numb))'''

#3%==0 jujs 5%==0 mugs 3 and 5 jujsmugs
numb=int((number := input("Enter the number: ")).isdigit() and number or (input("Kindly enter numeric value: ")))
print(((numb % 3 == 0) and (numb % 5 == 0) and "jugsmugs") or (numb % 3 == 0 and "jugs")or (numb % 5 == 0 and "mugs")  or numb)
#jujs mugs pugs
#jujs mugs
#jujs pugs
#mugs pugs
#jujs
#mugs
#pugs
numb=int((number := input("Enter the number: ")).isdigit() and number or (input("Kindly enter numeric value: ")))
print(((numb % 3 == 0) and (numb % 5 == 0)and (numb % 7 == 0) and "jugsmugspugs")or ((numb % 3 == 0) and (numb % 5 == 0) and "jugsmugs") or ((numb % 5 == 0) and (numb % 7 == 0) and "mugspugs") or (numb % 3 == 0 and "jugs")or (numb % 5 == 0 and "mugs") or (numb % 5 == 0 and "pugs")  or numb)