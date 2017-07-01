import Player, Dealer


class PlayBlackJack(object):

    def __init__(self):
        # Get number of players
        self.input = ''
        while not self.input.isnumeric():
            self.input = input('Welcome to Black-Jack!'
                               '\nHow many players will there be?')
        self.player_count = int(self.input)
        # Get player starting bankroll
        self.input = ''
        while not self.input.isnumeric():
            self.input = input('What is the buy-in?')
        self.starting_bankroll = int(self.input)

        self.player_list = []
        for p in range(int(self.player_count)):
            self.player_list.append(Player(self.starting_bankroll))

    this_player = Player()
    the_dealer = Dealer()
    while this_player.keep_playing:
    pass
