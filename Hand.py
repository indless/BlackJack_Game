class Hand(object):
    def __init__(self, player_bet=0, identity=0):
        self.bet = player_bet
        self.hand = []
        self.cardValue = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                          '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
        self.player_identity = identity
        self.handValue = 0
        self.aces = 0
        self.soft_aces = 0
        self.bust = False
        self.standing = False
        self.multiplier = 2

    def get_bet(self):
        return self.bet

    def get_card(self, num=1):
        if len(self.hand) >= num:
            return self.hand[num]

    def get_hand_value(self):
        # self.update_hand_value()
        return self.handValue

    def update_hand_value(self):
        self.handValue = 0
        self.soft_aces = self.aces
        for c in self.hand:
            self.handValue += self.cardValue[c[0]]
        if self.handValue > 21:
            for a in range(self.aces):
                self.handValue -= 10
                self.soft_aces -= 1
                if self.handValue <= 21:
                    break
        if self.handValue > 21:
            self.bust = True
            self.loss()

    def is_hand_soft(self):
        if self.soft_aces > 0:
            return True
        else:
            return False

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

    def split(self):
        if self.aces > 0:
            self.aces -= 1
        return self.hand.pop()

    def hit(self, a=()):
        if a[0] == 'Ace':
            self.aces += 1
        self.hand.append(a)
        self.update_hand_value()

    def stand(self):
        self.standing = True
        # self.update_hand_value()

    def payout(self):
        return self.bet * self.multiplier

    def loss(self):
        self.bet = 0

    def double(self, a=()):
        self.bet *= 2
        self.hit(a)
        self.stand()



