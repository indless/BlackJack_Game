import Bank_Roll, Player_Bet, Hand


class Player(object):

    def __init__(self, bankroll):
        self.my_Bank_Roll = Bank_Roll(bankroll)
        self.my_Bet = Player_Bet()
        self.myHand = Hand()
        self.input = ''

    def bet(self):
        while not self.input.isnumeric():
            self.input = input('Current balance ${b} '
                               '\nHow much would you like to bet? ').format(b=self.my_Bank_Roll.balance())

    def split(self):
        # split hand when identical value cards
        pass

    def double(self):
        # double bet on current hand
        pass

    def stand(self):
        # stay with current hand
        pass
