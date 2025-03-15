from typing import Dict, List, Tuple
from cards import Deck, CardList, Card

class Joker:
    def __init__(self, game: "Game") -> None:
        self.game = game

class plus2_mult(Joker):
    def effect(self) -> None:
        self.game.current_mult += 2

class Game:
    def __init__(self) -> None:
        self.references: Dict[str, Tuple[int, int]] = { # hand_pattern: (chips, mult)
            "0x": (5, 1),
            "0xx": (10, 2),
            "0xxyy": (20, 2),
            "0xxx": (30, 3),
            "0abcde": (30, 4),
            "100000": (35, 4),
            "0xxxyy": (40, 4),
            "0xxxx": (60, 7),
            "1abcde": (100, 8),
            "1ABCDE": (100, 8)
        }

        self.deck = Deck()
        self.consumables = []
        self.jokers: List[Joker] = []
        self.current_mult = 0
        self.curent_chips = 0
    
    def play_hand(self, hand: CardList) -> None:
        pass

if __name__ == "__main__":
    game = Game()
    c = Card
    game.play_hand(CardList([c("A", "C"), c("A", "S"), c("A", "H"), c("6", "S"), c("7", "S")]))
