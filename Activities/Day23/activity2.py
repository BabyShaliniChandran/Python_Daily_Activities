class BankAccount:
    def __init__(self,balance):
        self.__balance=5000
        self.__deposite=0
    @property
    def balance(self):
        return self.__balance
    @property
    def deposite(self):
        return self.__deposite
    @deposite.setter
    def deposite(self,amount):
        if amount>0:
            self.__balance=(amount+self.__balance)
            self.__deposite=amount
        else:
            print("amount is not sufficient")
    @property
    def withraw(slef,amount):
        if amount>= 0:
            if amount>= self.__balance:
                self.__balance-=amount
amount=BankAccount(200)
amount.deposite=1000
print(amount.balance)

amount.withraw(2000)
print(amount.balance)

