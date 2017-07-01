class Deck(object):
    def __init__(self):
        self.deck = []
        self.cardType = ['Ace 2 3 4 5 6 7 8 9 10 Jack Queen King'.split()]
        self.cardSuit = ['Spade', 'Club', 'Diamond', 'Heart']
        for c in self.cardType:
            for s in self.cardSuit:
                self.deck.append((c, s))
                