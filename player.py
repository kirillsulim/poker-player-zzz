import sys

class Player:
    VERSION = "zzz-print-9999-getp"

    def get_player(self, game_state, name):
        for player in game_state.players:
            if player.name == name:
                return player

    def betRequest(self, game_state):
        try:
            print 'a'
            print game_state
            print 'me'
            print get_player(self, game_state, self.VERSION)
            sys.stdout.write(game_state)
            sys.stderr.write(game_state)
            return 9999
        except Exception:
            return 9999

    def showdown(self, game_state):
        pass



