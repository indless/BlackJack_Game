class BankRoll(object):

    def __init__(self, bank):
        self.bank = bank

    def balance(self):
        return self.bank

    def deposit(self, deposit):
        self.bank += deposit

    def withdraw(self, withdraw):
        self.bank -= withdraw
