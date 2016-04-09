import sys

class Player:
    VERSION = "zzz-print"

    def betRequest(self, game_state):
        try:
            print 'a'
            print game_state
            sys.stdout.write(game_state)
            sys.stderr.write(game_state)
            return 999
        except Exception:
            return 999

    def showdown(self, game_state):
        pass

