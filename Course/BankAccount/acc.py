class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


account=Account("balance.txt")
print('$' + str(account.balance))
account.withdraw(500)
print('$' + str(account.balance))
account.deposit(501)
print('$' + str(account.balance))

account.commit(Account) #By putting the account in the parenthesis it is inheriting

class CheckingAccount:

    def __init__ (self, filepath, fee): #Inherits the Account Class' init method
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


checkingAcc = CheckingAccount('balance.txt')
print(checkingAcc.balance)