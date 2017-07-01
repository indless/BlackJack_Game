import Deck, Hand


class Dealer(object):
    def __init__(self):
        self.the_deck = Deck()
        self.dealer_hand = Hand()
        self.the_deck.shuffle()

    def deal_initial(self):
        self.the_deck.next_card()

    def deal(self):
        self.the_deck.next_card()
