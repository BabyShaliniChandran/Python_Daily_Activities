#3%==0 jujs 5%==0 mugs 3 and 5 jujsmugs
numb=int((number := input("Enter the number: ")).isdigit() and number or (input("Kindly enter numeric value: ")))
print(((numb % 3 == 0) and (numb % 5 == 0) and "jugsmugs") or (numb % 3 == 0 and "jugs")or (numb % 5 == 0 and "mugs")  or numb)