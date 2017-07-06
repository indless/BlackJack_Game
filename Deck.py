import random


class Deck(object):
    def __init__(self):
        self.deck = []
        self.deck_shuffled = []
        self.cardValue = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                          '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
        self.cardType = 'Ace 2 3 4 5 6 7 8 9 10 Jack Queen King'.split()
        self.cardSuit = ['Spade', 'Club', 'Diamond', 'Heart']
        for c in self.cardType:
            for s in self.cardSuit:
                self.deck.append((c, s))

    def shuffle(self):
        self.deck_shuffled = []
        for c in self.deck:
            self.deck_shuffled.append(c)

        random.shuffle(self.deck_shuffled)

    def next_card(self):
        return self.deck_shuffled.pop()

    def cards_remaining(self):
        return len(self.deck)
