from typing import List

from cards import CardList


class Texas:
    def __init__(self, player_list: List[CardList]) -> None:
        self.set_players(player_list)

    def set_players(self, player_list: List[CardList]) -> None:
        self.players = player_list

if __name__ == "__main__":
    pass
