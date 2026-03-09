import random


class RamsEngine:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def deal_cards(self, player_count):
        deck = [{"suit": s, "rank": r} for s in self.suits for r in self.ranks]
        random.shuffle(deck)
        hands = [deck[i * 5:(i + 1) * 5] for i in range(player_count)]
        trump = deck[player_count * 5]
        return hands, trump

    def identify_winner(self, played_cards, trump_suit):
        leading_suit = played_cards[0][1]['suit']

        def card_value(card):
            val = {'7': 7, '8': 8, '9': 9, '10': 10,
                   'J': 11, 'Q': 12, 'K': 13, 'A': 14}[card['rank']]
            if card['suit'] == trump_suit:
                val += 100
            elif card['suit'] == leading_suit:
                val += 20
            return val

        return max(played_cards, key=lambda x: card_value(x[1]))[0]

