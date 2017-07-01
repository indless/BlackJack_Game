import Deck, Hand, Player


class Dealer(object):
    def __init__(self):
        self.the_deck = Deck()
        self.dealer_hand = Hand()
        self.dealer_visible_card = ()
        self.the_deck.shuffle()
        self.player_hands = []

        # Get number of players
        self.input = ''
        while not self.input.isnumeric():
            self.input = input('Welcome to Black-Jack!'
                               '\nHow many players will there be? ')
        self.player_count = int(self.input)
        # Get player starting bankroll
        self.input = ''
        while not self.input.isnumeric():
            self.input = input('What is the buy-in?')
        self.starting_bankroll = int(self.input)

        # add each player to list along with starting bankroll and Identifying number
        self.player_list = []
        for p in range(int(self.player_count)):
            self.player_list.append(Player(self.starting_bankroll, p))
            self.player_list[p].set_name()

    def deal_round(self):
        # get player bets
        for p in self.player_list:
            p.bet()

        # identify each hand to the corresponding player and bet value and deal first card
        for p in self.player_list:
            self.player_hands = (Hand(p.get_bet, p.identity))
            self.player_hands[p.identity].hit(self.the_deck.next_card())
        # gives dealer first card
        self.dealer_hand = Hand(0, -1)
        self.dealer_hand.hit(self.the_deck.next_card())

        # deal second card to each hand
        for h in self.player_hands:
            h.hit(self.the_deck.next_card())
        # deal second card to dealer
        self.dealer_hand.hit(self.the_deck.next_card())
        self.dealer_visible_card = self.dealer_hand.hand[1]

        # is dealer showing Ace?
        if self.dealer_visible_card[0] == 'Ace':
            print('Dealer showing {ace} \nChecking for Black-Jack'.format(ace=self.dealer_visible_card))
            if self.dealer_hand.black_jack():
                print('Dealer Black-Jack! Dealer Wins!')
                for h in self.player_hands:
                    if not h.black_jack():
                        self.hand_loses(h)
                    else:
                        # payout any players with Black Jack
                        self.hand_wins(h)
            else:
                print('No dealer Black-Jack')

        # player(s) turn
        for h in self.player_hands:
            print(h.hand)
            if h.black_jack():
                print('Black-Jack!!!')
                self.hand_wins(h)
            else:
                while not h.standing or not h.bust:
                    self.get_player_move(h)
                if h.bust:
                    print('Busted!')
                else:
                    print('Standing with {hv}'.format(hv=h.get_hand_value()))

    def hand_loses(self, hand):
        hand.bust = True
        hand.loss()
        print('Sorry {name}, you lost this hand.'.format(name=self.player_list[hand.palyer_identity]))

    def hand_wins(self, hand):
        self.player_list[hand.player_identity].deposit(hand.payout())
        print('Congratulations {name}, you won ${payout}!'.format(name=self.player_list[hand.palyer_identity],
                                                                  payout=hand.payout()))

    def get_player_move(self, hand):
        self.input = ''
        while self.input not in 'hit double split stand'.split():
            self.input = input('{name}, you have {hv}, what would you like to do? (hit, double, split or stand)'
                               .format(name=self.player_list[hand.player_identity].get_name(),
                                       hv=hand.get_hand_value())).lower()

    def hit(self):
        # take additional card
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
