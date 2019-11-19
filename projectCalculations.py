class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank # from 0 to 12
        self.suit = suit # from 0 to 3


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in ['D', 'H', 'S', 'C']:
            for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                        'J', 'Q', 'K']:
                self.cards.append(Card(rank, suit))

    def cardsLeft(self):
        return self.cards

def TexasHoldem():
    deck = Deck()
    count = 0
    playerHand = []
    while count != 5:
        count += 1
        # asked for cards
        if count <= 2:
            card  = input('What card is in your hand?(enter rank, then one of SDCH for suit)')
        else:
            card = input('What card is on the table?(enter rank, then one of SDCH for suit)')
        # makes the card for input
        if len(card) >=2:
            if card[1] == '0':
                enteredCard = Card('T', card[1].upper())
            else:
                enteredCard = Card(card[0], card[1].upper())
        else:
            enteredCard = Card(19, 'none')
        # adds to deck if valid
        for card in  deck.cardsLeft():
            print(card.rank, card.suit)
        if enteredCard in deck.cardsLeft():
            print('added to your deck')
            playerHand.append(enteredCard)
        else:
            if count > 0: count -= 1
            print('that is an invalid card')
        
        

    

TexasHoldem()