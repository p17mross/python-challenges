import random

class Card:
    SUIT_NAMES = ["Spades", "Hearts", "Diamonds", "Clubs"]
    CARD_NAMES = [
        "Ace", 
        "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
        "Jack", "Queen", "King"
    ]

    suit: int
    value: int

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self) -> str:
        return Card.CARD_NAMES[self.value] + " of " + Card.SUIT_NAMES[self.suit]

def shuffle():
    cards = []

    for suit in range(4):
        for value in range(13):
            cards.append(Card(suit, value))

    random.shuffle(cards)

    return cards    

cards = shuffle()
for card in cards:
    print(card)
