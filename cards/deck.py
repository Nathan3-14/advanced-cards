from typing import List
from .card import Card

class CardList(List):
    def get_cards(self, suit: str="", value: str=""):
        output = []
        for card in self:
            output.append(card)
        return output

class Deck:
    def __init__(self, values: str="A,1,2,3,4,5,6,7,8,9,10,J,Q,K", suits: str="S,C,D,H") -> None:
        self.suits = suits
        self.values = values
        self.deck = CardList([])
        for suit in suits.split(","):
            for value in values.split(","):
                self.deck.append(Card(value, suit))

    def display_deck(self, suited: bool=False):
        if suited:
            for suit in self.suits:
                print(", ".join([str(card) for card in self.deck.get_cards(suit=suit)]))
        else:
            print(", ".join([str(card) for card in self.deck]))
