import sys

class Player:
    VERSION = "zzz-print-9999-getp-hand"

    def get_player(self, game_state, name):
        for player in game_state.players:
            if player.name == name:
                return player

    def get_hand(self, player):
        return player.hole_cards

    def is_ace(self, cards):
        result = ""
        for card in cards:
            result += card.rank

        if cards[0].suit == cards[1].suit:
            result += 'S'
        else:
            result += 'O'

    def betRequest(self, game_state):
        try:
            print 'a'
            print game_state
            print 'me'
            player = self.get_player(game_state, self.VERSION)
            print player
            print 'hand'
            print self.get_hand(player)
            sys.stdout.write(game_state)
            sys.stderr.write(game_state)
            return 9999
        except Exception:
            return 9999

    def showdown(self, game_state):
        pass





