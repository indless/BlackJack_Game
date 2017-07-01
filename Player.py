import Hand


class Player(object):

    def __init__(self, bank):
        self.hand_history = []
        self.input = ''
        self.bank = bank
        self.hand = Hand()
        self.name = ''

    def get_name(self):
        while True:
            self.name = input('Hello! What is your name? ')
            

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

    def play_hand(self):
        # initiates a hand given the input bet

        pass

    def split(self):
        # split hand when identical value cards
        pass

    def double(self):
        # double bet on current hand
        pass

    def stand(self):
        # stay with current hand
        pass
