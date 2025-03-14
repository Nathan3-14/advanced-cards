from rich.console import Console
from cards import Deck, check, CardList, Card

class TestGame:
    def __init__(self) -> None:
        self.deck = Deck()

if __name__ == "__main__":
    game = TestGame()
    nothing_list = CardList([
        Card("J", "C"),
        Card("6", "S"),
        Card("A", "H"),
        Card("K", "H"),
        Card("9", "D")
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
    straight_ace_A = CardList([
        Card("A", "D"),
        Card("2", "H"),
        Card("3", "H"),
        Card("4", "C"),
        Card("5", "D")
    ])
    straight_ace_B = CardList([
        Card("A", "D"),
        Card("K", "H"),
        Card("J", "H"),
        Card("10", "C"),
        Card("Q", "D")
    ])
    straight_ace_C = CardList([
        Card("A", "D"),
        Card("K", "H"),
        Card("3", "H"),
        Card("2", "C"),
        Card("Q", "D")
    ])
    # game.deck.display_deck(suited=True)
    print("Pair T: " + str(check(pair_twopair_test_list, "0xx")))
    print("Pair F: " + str(check(nothing_list, "0xx")) + "\n")
    print("Two Pair T: " + str(check(pair_twopair_test_list, "0xxyy")))
    print("Two Pair F: " + str(check(nothing_list, "0xxyy")) + "\n")
    print("Straight T: " + str(check(flush_straight_straightflush_test_list, "0abcde")))
    # print("Straight A-T: " + str(check(straight_ace_A, "0abcde")))
    # print("Straight B-T: " + str(check(straight_ace_B, "0abcde")))
    # print("Straight C-F: " + str(check(straight_ace_C, "0abcde")))
    print("Straight F: " + str(check(nothing_list, "0abcde")) + "\n")
    print("Flush T: " + str(check(flush_straight_straightflush_test_list, "10000")))
    print("Flush F: " + str(check(nothing_list, "10000")) + "\n")
    print("Straight Flush T: " + str(check(flush_straight_straightflush_test_list, "1abcde")))
    print("Straight Flush F: " + str(check(nothing_list, "1abcde")) + "\n")
    print("Royal Flush T: " + str(check(CardList([Card("10", "C"), Card("J", "C"), Card("Q", "C"), Card("K", "C"), Card("A", "C")]), "1ABCDE")))
    print("Royal Flush F: " + str(check(CardList([Card("9", "C"), Card("10", "C"), Card("J", "C"), Card("Q", "C"), Card("K", "C")]), "1ABCDE")) + "\n")
