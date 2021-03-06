class Player(object):

    def __init__(self, bank=100, identity=0):
        self.hand_history = []
        self.input = ''
        self.bank = bank
        self.hand = []
        self.name = ''
        self.identity = identity
        self.bet = 0

    def set_name(self):
        self.name = input('Hello player #{i}! What is your name? '.format(i=self.identity + 1))
        print('Nice to meet you {name}!'.format(name=self.name))

    def get_name(self):
        return self.name

    def balance(self):
        return self.bank

    def deposit(self, deposit):
        self.bank += deposit

    def withdraw(self, withdraw):
        self.bank -= withdraw

    def make_bet(self):
        self.input = ''
        self.bet = 0
        while True:
            while not self.input.isnumeric():
                self.input = input('{name}, current balance: ${b} '
                                   '\nHow much would you like to bet? '.format(name=self.get_name(), b=self.balance()))
            self.bet = int(self.input)
            if self.bet <= self.bank:
                break
            else:
                self.input = ''

    def get_bet(self):
        self.withdraw(self.bet)
        return self.bet
