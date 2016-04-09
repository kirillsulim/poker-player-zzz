import sys

class Player:
    VERSION = "zzz-print-9999"

    def betRequest(self, game_state):
        try:
            print 'a'
            print game_state
            sys.stdout.write(game_state)
            sys.stderr.write(game_state)
            return 9999
        except Exception:
            return 9999

    def showdown(self, game_state):
        pass

