class Player(object):

    def __init__(self, bank, identity=0):
        self.hand_history = []
        self.input = ''
        self.bank = bank
        self.hand = []
        self.name = ''
        self.identity = identity
        self.bet = 0

    def set_name(self):
        self.name = input('Hello player #{i}! What is your name? '.format(self.identity + 1))
        print('Nice to meet you {name]!'.format(name=self.name))

    def get_name(self):
        return self.name

    def balance(self):
        return self.bank

    def deposit(self, deposit):
        self.bank += deposit

    def withdraw(self, withdraw):
        self.bank -= withdraw

    def bet(self):
        while not self.input.isnumeric():
            self.input = input('Current balance ${b} '
                               '\nHow much would you like to bet? '.format(b=self.balance()))
        self.bet = int(self.input)

    def get_bet(self):
        self.withdraw(self.bet)
        return self.bet

    def play_hand(self):
        # initiates a hand given the input bet

        pass

