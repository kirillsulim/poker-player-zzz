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
            result += 's'
        else:
            result += 'o'
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
        if self.hand_in_range(cards_str, 3):
            return 9999
        else:
            return 0

    ARR = [
        'AA',
        'KK',
        'AKs',
        'QQ',
        'AKo',
        'JJ',
'AQs',
'TT',
'AQo',
'99',
'AJs',
'88',
'ATs',
'AJo',
'77',
'66',
'ATo',
'A9s',
'55',
'A8s',
'KQs',
'44',
'A9o',
'A7s',
'KJs',
'A5s',
'A8o',
'A6s',
'A4s',
'33',
'KTs',
'A7o',
'A3s',
'KQo',
'A2s',
'A5o',
'A6o',
'A4o',
'KJo',
'QJs',
'A3o',
'22',
'K9s',
'A2o',
'KTo',
'QTs',
'K8s',
'K7s',
'JTs',
'K9o',
'K6s',
'QJo',
'Q9s',
'K5s',
'K8o',
'K4s',
'QTo',
'K7o',
'K3s',
'K2s',
'Q8s',
'K6o',
'J9s',
'K5o',
'Q9o',
'JTo',
'K4o',
'Q7s',
'T9s',
'Q6s',
'K3o',
'J8s',
'Q5s',
'K2o',
'Q8o',
'Q4s',
'J9o',
'Q3s',
'T8s',
'J7s',
'Q7o',
'Q2s',
'Q6o',
'98s',
'Q5o',
'J8o',
'T9o',
'J6s',
'T7s',
'J5s',
'Q4o',
'J4s',
'J7o',
'Q3o',
'97s',
'T8o',
'J3s',
'T6s',
'Q2o',
'J2s',
'87s',
'J6o',
'98o',
'T7o',
'96s',
'J5o',
'T5s',
'T4s',
'86s',
'J4o',
'T6o',
'97o',
'T3s',
'76s',
'95s',
'J3o',
'T2s',
'87o',
'85s',
'96o',
'T5o',
'J2o',
'75s',
'94s',
'T4o',
'65s',
'86o',
'93s',
'84s',
'95o',
'T3o',
'76o',
'92s',
'74s',
'54s',
'T2o',
'85o',
'64s',
'83s',
'94o',
'75o',
'82s',
'73s',
'93o',
'65o',
'53s',
'63s',
'84o',
'92o',
'43s',
'74o',
'72s',
'54o',
'64o',
'52s',
'62s',
'83o',
'42s',
'82o',
'73o',
'53o',
'63o',
'32s',
'43o',
'72o',
'52o',
'62o',
'42o',
'32o',
        ]

    def hand_in_range(self, hand, a_range):
        max_m = a_range * 13.56
        end = 0
        i = 0

        while end < max_m:
            i += 1
            if self.ARR[i] == hand:
                return True
            if self.ARR[i][0] == self.ARR[i][1]:
                end += 6
            elif self.ARR[i][2] == 's':
                end += 12
            elif self.ARR[i][2] == 'o':
                end += 4

        return False








