from rich.console import Console
from cards import Deck

class TestGame:
    def __init__(self) -> None:
        self.deck = Deck()

if __name__ == "__main__":
    game = TestGame()
    game.deck.display_deck(suited=True)
