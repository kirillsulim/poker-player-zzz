import sys

class Player:
    VERSION = "zzz"

    def betRequest(self, game_state):
        try:
            sys.stdout.write(game_state)
            sys.stderr.write(game_state)
            return 50
        except Exception:
            return 999

    def showdown(self, game_state):
        pass

