from rich.console import Console
from cards import Deck, check, CardList, Card

class TestGame:
    def __init__(self) -> None:
        self.deck = Deck()

if __name__ == "__main__":
    game = TestGame()
    nothing_list = CardList([
        Card("J", "C"),
        Card("5", "S"),
        Card("6", "H"),
        Card("K", "H")
    ])
    pair_twopair_test_list = CardList([
        Card("2", "H"),
        Card("2", "C"),
        Card("3", "H"),
        Card("3", "S"),
        Card("J", "S")
    ])
    flush_straight_straightflush_test_list = CardList([
        Card("4", "H"),
        Card("5", "H"),
        Card("6", "H"),
        Card("7", "H"),
        Card("8", "H")
    ])
    # game.deck.display_deck(suited=True)
    print("Pair T: " + str(check(pair_twopair_test_list, "0x0x")))
    print("Pair F: " + str(check(nothing_list, "0x0x")) + "\n")
    print("Two Pair T: " + str(check(pair_twopair_test_list, "0x0x0y0y")))
    print("Two Pair F: " + str(check(nothing_list, "0x0x0y0y")) + "\n")
    print("Straight T: " + str(check(flush_straight_straightflush_test_list, "0a0b0c0d0e")))
    print("Straight F: " + str(check(nothing_list, "0a0b0c0d0e")) + "\n")
    print("Flush T: " + str(check(flush_straight_straightflush_test_list, "10101010")))
    print("Flush F: " + str(check(nothing_list, "10101010")) + "\n")
    print("Straight Flush T: " + str(check(flush_straight_straightflush_test_list, "1a1b1c1d1e")))
    print("Straight Flush F: " + str(check(nothing_list, "1a1b1c1d1e")) + "\n")
