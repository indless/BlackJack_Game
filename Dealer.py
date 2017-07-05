from Deck import Deck
from Hand import Hand
from Player import Player


class Dealer(object):
    def __init__(self):
        self.the_deck = Deck()
        self.dealer_hand = Hand()
        self.dealer_visible_card = ()
        self.the_deck.shuffle()
        self.player_hands = []
        self.another_round = True

        # Get number of players
        self.input = ''
        while not self.input.isnumeric():
            self.input = input('Welcome to Black-Jack!'
                               '\nHow many players will there be? ')
        self.player_count = int(self.input)
        # Get player starting bankroll
        self.input = ''
        while not self.input.isnumeric():
            self.input = input('What is the buy-in? ')
        self.starting_bankroll = int(self.input)

        # add each player to list along with starting bankroll and Identifying number
        self.player_list = []
        for p in range(int(self.player_count)):
            self.player_list.append(Player(self.starting_bankroll, p))
            self.player_list[p].set_name()

    def deal_round(self):
        # get player bets
        for p in self.player_list:
            p.make_bet()

        # identify each hand to the corresponding player and bet value and deal first card
        for p in self.player_list:
            self.player_hands.append(Hand(p.get_bet, p.identity))
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
            print('Dealer showing {ace} \nChecking for Black-Jack...'.format(ace=self.dealer_visible_card))
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
            if h.black_jack():
                print('Black-Jack!!!')
                self.hand_wins(h)
            else:
                while not h.standing or not h.bust:
                    self.get_player_move(h)

        # dealer's turn
        self.dealer_plays_hand()

        # determine winning player hands & make payouts
        for h in self.player_hands:
            if h.get_hand_value() > self.dealer_hand.get_hand_value():
                self.hand_wins(h)
            elif h.get_hand_value() == self.dealer_hand.get_hand_value():
                self.push(h)
            else:
                self.hand_loses(h)

        # allows only one hand to be played
        self.another_round = False

    def hand_loses(self, hand):
        hand.bust = True
        hand.loss()
        print('Sorry {name}, dealer has Black-Jack. You lost this hand.'.format(name=self.player_list[hand.palyer_identity]))

    def push(self, hand):
        # player ties with dealer, return bet to player
        self.player_list[hand.player_identity].deposit(hand.bet)
        print('It\'s a Push. Your bet of ${bet} was returned.'.format(name=self.player_list[hand.palyer_identity],
                                                                  bet=hand.bet))

    def hand_wins(self, hand):
        self.player_list[hand.player_identity].deposit(hand.payout())
        print('Congratulations {name}, you won ${payout}!'.format(name=self.player_list[hand.palyer_identity],
                                                                  payout=hand.payout()))

    def get_player_move(self, hand):
        # player plays hand
        self.input = ''
        while self.input not in 'hit double split stand'.split():
            print(hand.hand)
            self.input = input('{name}, you have {hv}, what would you like to do? (hit, double, split or stand)'
                               .format(name=self.player_list[hand.player_identity].get_name(),
                                       hv=hand.get_hand_value())).lower()
        self.make_player_move(hand)

        # Player stands or busts
        if hand.bust:
            print('{hv}, Busted!'.format(hv=hand.get_hand_value()))
        else:
            print('Standing with {hv}'.format(hv=hand.get_hand_value()))

    def make_player_move(self, hand):
        if self.input == 'hit':
            self.hit(hand)
        elif self.input == 'double':
            # if self.player_list[hand.player_identity].balance() >= hand.bet:
            if self.player_list[hand.player_identity].bank >= hand.bet:
                self.double(hand)
            else:
                print('Insufficient funds, unable to double bet')
        elif self.input == 'split':
            if self.player_list[hand.player_identity].balance() >= hand.bet:
                self.split(hand)
            else:
                print('Insufficient funds, unable to split hand')
        elif self.input == 'stand':
            self.stand(hand)

    def dealer_plays_hand(self):
        # dealer plays hand
        # dealer hits on 15 or soft 16, stands if greater
        pass

    def hit(self, hand):
        # take additional card
        hand.hit(self.the_deck.next_card())

    def split(self, hand):
        # split hand when identical value cards
        split_hand = Hand(hand.bet, hand.player_identity)
        # insert new hand into self.player_hands at current index +1 & copy Hand.identity to new hand
        # will need to also withdraw BET amount from Player bankroll equal to Hand.bet
        self.player_hands.insert(self.player_hands.index(hand)+1, split_hand)

        # inserts one of the cards from 'hand' into 'split_hand'
        split_hand.hit(hand.split())
        # give each hand a second card
        hand.hit(self.the_deck.next_card())
        split_hand.hit(self.the_deck.next_card())

    def double(self, hand):
        # double bet on current hand
        hand.double(self.the_deck.next_card())

    def stand(self, hand):
        # stay with current hand
        hand.stand()

    def remove_player(self):
        # if player bank = 0 after a round, or player bets 0 then
        # remove player from player list with self.player_list.remove(p)
        pass

the_dealer = Dealer()
while the_dealer.another_round:
    the_dealer.deal_round()
