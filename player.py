#import traceback
import sys


class Player:
    VERSION = "zzz-anam"
    NAME = "zzz"

    def get_player(self, game_state, name):
        for player in game_state['players']:
            if player['name'] == self.VERSION or player['name'] == self.NAME:
                return player

    def get_hand(self, player):
        return player['hole_cards']

    def as_str(self, cards):
        result = ""
        for card in cards:
            if card['rank'] == '10':
                result += 'T'
            else:
                result += card['rank']

        result = self.sort(result)

        if result[0] == result[1]:
            return result

        if cards[0]['suit'] == cards[1]['suit']:
            result += 'S'
        else:
            result += 'O'
        return result

    def betRequest(self, game_state):
        try:
            sys.stdout.write('Sout')
            sys.stderr.write('Serr')
            print 'a'
            print game_state
            print 'me'
            player = self.get_player(game_state, self.VERSION)
            print player
            print 'hand'
            cards = self.get_hand(player)
            print cards
            zaza = self.as_str(cards)
            print zaza
            return self.win(zaza)
        except Exception as e:
            print e
            # traceback.print_exc()
            return 9999

    def showdown(self, game_state):
        pass

    ORDER = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    def sort(self, cards):
        if self.ORDER.index(cards[0]) < self.ORDER.index(cards[1]):
            return cards
        else:
            return cards[1] + cards[0]

    def win(self, cards_str):
        if cards_str[0] == 'A':
            return 9999
        else:
            return 0





