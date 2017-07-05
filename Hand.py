class Hand(object):
    def __init__(self, bet=0, identity=0):
        self.bet = bet
        self.hand = []
        self.cardValue = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                          '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
        self.player_identity = identity
        self.handValue = 0
        self.aces = 0
        self.bust = False
        self.standing = False
        self.multiplier = 2

    #def starting_hand(self, a=(), b=()):
    #    self.hand.append(a)
    #    self.hand.append(b)

    def get_card(self, num=1):
        if len(self.hand) >= num:
            return self.hand[num]

    def get_hand_value(self):
        self.update_hand_value()
        return self.handValue

    def update_hand_value(self):
        self.handValue = 0
        for c in self.hand:
            # print(c[0])
            self.handValue += self.cardValue[c[0]]
        if self.handValue > 21:
            for a in range(self.count_aces()):
                self.handValue -= 10
                if self.handValue <= 21:
                    break
        if self.handValue > 21:
            self.bust = True
            self.loss()

    def count_aces(self):
        if self.hand.count('Ace') > 0:
            self.aces = self.hand.count('Ace')
        else:
            self.aces = 0

    def black_jack(self):
        if len(self.hand) == 2:
            self.get_hand_value()
            if self.handValue == 21:
                self.multiplier = 2.5
                self.standing = True
                return True
        return False

    def can_split(self):
        if self.hand[0][0] == self.hand[1][0] and len(self.hand) == 2:
            return True
        else:
            return False

    def split_hand(self):
        return self.hand.pop()

    def hit(self, a=()):
        self.hand.append(a)
        self.update_hand_value()

    def stand(self):
        self.standing = True
        self.update_hand_value()

    def payout(self, multiplier):
        return self.bet * multiplier

    def loss(self):
        self.bet -= self.bet

    def double(self, a=()):
        self.bet += self.bet
        self.hit(a)
        self.stand()



