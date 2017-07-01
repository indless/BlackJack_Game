class Player_Bet(object):

    def __init__(self, bet):
        self.bet = bet

    def payout(self, multiplyer):
        self.bet *= multiplyer

    def loss(self):
        self.bet -= self.bet