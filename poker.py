from typing import List
from cards import CardList, Deck, check

class Game:
    def __init__(self, player_list: List[str]) -> None:
        self.hands = {
            player_name: CardList() for player_name in player_list
        }
        self.deck = Deck()
    
    def get_player(self, player_name) -> CardList:
        return self.hands[player_name]

class FiveCard(Game):
    def __init__(self, players: List[str]) -> None:
        super().__init__(player_list=players)
    
    def round(self) -> None:
        pass
    

class Texas(Game):
    def __init__(self, players: List[str]) -> None:
        super().__init__(player_list=players)
        self.community_cards = CardList()

if __name__ == "__main__":
    players = ["A", "B", "C", "D"]
    game = FiveCard(players=players)
    # game = Texas(players=players)
