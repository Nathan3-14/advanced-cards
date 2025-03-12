class Card():
    def __init__(self, value: str, suit: str) -> None:
        self.value = value
        self.suit = suit
    
    def __str__(self) -> str:
        return f"{self.suit} {self.value}"
        