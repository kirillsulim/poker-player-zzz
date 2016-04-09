
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            return 9999
        except Exception e:
            print e
            return 0

    def showdown(self, game_state):
        print game_state

