#update the balance
#name,account_no,pan_card,balance,credited_amount,debited_amount
'''account_info=('Shalini','zxy12345','123456fsdg',[300,200,300])
action=input("Enter the credit or debit action:")
amount=int(input("enter the amount:"))
action == "debit" and account_info[3][0]:=account_info[3][0]-amount
action == "debit" and account_info[3][-1]=account_info[3][-1]+amount
action == "credit" and account_info[3][0]=account_info[3][0]+amount
action == "credit" and account_info[3][1]=account_info[3][1]+amount
print(account_info)'''

account_info = ('Shalini', 'zxy12345', '123456fsdg', [300, 200, 300])
action = input("Enter the credit or debit action: ")
amount = int(input("Enter the amount: "))

action == "debit" and (account_info[3][0] = account_info[3][0] - amount)
action == "debit" and (account_info[3][-1] = account_info[3][-1] + amount)
action == "credit" and (account_info[3][0] = account_info[3][0] + amount)
action == "credit" and (account_info[3][1] = account_info[3][1] + amount)

print(account_info)



