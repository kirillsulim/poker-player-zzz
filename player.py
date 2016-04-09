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
            print 'sb'
            small_blind = self.get_small_blind(game_state)
            print small_blind
            print 'bets'
            bets = self.get_player_bets(game_state)
            print bets
            print 'raise'
            pot2 = self.get_pot2_or_min(game_state)
            print pot2
            print 'stack'
            stack = self.get_stack(player)
            print stack
            print 'tob and count'
            tob, count = self.get_to_small_blind(game_state)
            print tob
            print count
            return self.win(zaza, small_blind, bets, pot2, stack, tob, count)
        except Exception as e:
            print e
            # traceback.print_exc()
            return 9999

    def showdown(self, game_state):
        pass

    def get_small_blind(self, game_state):
        return game_state['small_blind']

    def get_player_bets(self, game_state):
        result = []
        for player in game_state['players']:
            result.append(player['bet'])
        return result

    ORDER = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    def sort(self, cards):
        if self.ORDER.index(cards[0]) < self.ORDER.index(cards[1]):
            return cards
        else:
            return cards[1] + cards[0]

    def win(self, cards_str, small_blind, bets, pot2, stack, tob, count):
        raised = False
        all_zero_ex_blinds = True
        big_b_25 = small_blind * 2.5 * 2
        for bet in bets:
            if bet > big_b_25:
                raised = True
            if bet > 2 * small_blind:
                all_zero_ex_blinds = False

        if all_zero_ex_blinds and count <= 4 and stack > 50 * small_blind * 2:
            return 4 * small_blind

        calc_range = self.calc_range(small_blind * 2, stack) * self.calc_sb(tob)

        if raised:
            if self.hand_in_range(cards_str, 0.5 * calc_range):
                return 9999
            else:
                return 0
        elif self.hand_in_range(cards_str, calc_range):
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
        i = 0

        while i < max_m:
            i += 1
            if self.ARR[i] == hand:
                return True
            if self.ARR[i][0] == self.ARR[i][1]:
                i += 6
            elif self.ARR[i][2] == 's':
                i += 12
            elif self.ARR[i][2] == 'o':
                i += 4

        return False

    def get_to_small_blind(self, game_state):
        small_blind = self.get_small_blind(game_state)
        count = 0
        me_index = 0
        sb_index = 0

        for player in game_state['players']:
            if player['status'] == 'active':
                count += 1
            if player['bet'] == small_blind:
                sb_index = count
            if player['name'] == self.NAME or player['name'] == self.VERSION:
                me_index = count

        if me_index <= sb_index:
            return sb_index - me_index, count
        else:
            return count - sb_index + me_index, count

    def get_pot2_or_min(self, game_state):
        pot = game_state['pot'] * 2
        min_r = game_state['minimum_raise']
##
        if min_r > pot:
            return min_r
        else:
            return pot


    def get_sb_player(self, game_state):
        small_b = self.get_small_blind(game_state)
        for player in game_state['players']:
            if player['bet'] == small_b:
                return player

    def get_stack(self, player):
        return player['stack']

    def calc_range(self, big_blind, stack):
        base = 1
        if stack < 10 * big_blind:
            return base * 16
        elif stack < 20 * big_blind:
            return base * 9
        elif stack < 30 * big_blind:
            return base * 6
        elif stack < 50 * big_blind:
            return base * 4
        elif stack < 100 * big_blind:
            return base * 2
        return base

    def calc_sb(self, tosb):
        if tosb == 0:
            return 7
        elif 1:
            return 4
        #elif 2:
         #   return 2
        return 1







