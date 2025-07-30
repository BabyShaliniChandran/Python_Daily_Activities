'''
temp=37
advice="see a doctor" if 37 >38 else "Rest and hydrate"
print(advice)

print("see a doctor" if int(input("enter the temp:")) >38 else "Rest and hydrate")


print("see a doctor" and int(input("enter the temp:")) >38 or "Rest and hydrate")

advice=((temp=37) >38) and "see a doctor" or "Rest and hydrate"
'''

advice="see a doctor" if (temp:=37) >38 else "Rest and hydrate"

advice=(temp:=37) >38 and "see a doctor" else "Rest and hydrate"