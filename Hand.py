class Hand(object):
    def __init__(self, bet):
        self.bet = bet
        self.hand = []
        self.cardValue = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                          '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
        self.handValue = 0
        self.aces = 0
        self.bust = False
        self.standing = False
        self.multiplier = 2

    def starting_hand(self, a=(), b=()):
        self.hand.append(a)
        self.hand.append(b)

    def get_hand_value(self):
        self.handValue = 0
        for c in self.hand:
            self.handValue += self.cardValue[self.hand[c][0]]
        if self.handValue > 21:
            for a in range(self.count_aces()):
                self.handValue -= 10
                if self.handValue <= 21:
                    break
        if self.handValue > 21:
            self.bust = True
            self.loss()

    def count_aces(self):
        self.aces = self.hand.count('Ace')

    def black_jack(self):
        if len(self.hand) == 2:
            self.get_hand_value()
            if self.handValue == 21:
                self.multiplier = 2.5

    def can_split(self):
        if self.hand[0][0] == self.hand[1][0]:
            return True
        else:
            return False

    def split_hand(self):
        return self.hand.pop()

    def hit(self, a=()):
        self.hand.append(a)
        self.get_hand_value()

    def stand(self):
        self.standing = True
        self.get_hand_value()

    def payout(self, multiplier):
        self.bet *= multiplier

    def loss(self):
        self.bet -= self.bet

    def double(self, a=()):
        self.bet += self.bet
        self.hit(a)
        self.stand()



