from typing import Any, Dict
from .deck import CardList, Deck
from rich.console import Console

def _remove_from_dict(_value: Any, _dict: Dict[Any, Any]) -> None:
    for key, value in _dict.items():
        if value == _value:
            del _dict[key]
            return

def check(cardlist: CardList, pattern: str, deck: Deck=Deck()) -> bool:
    console = Console()
    index = 1
    pattern_check_suit = pattern[0] == "1"
    values_present = {}
    
    sort_order = {"2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7, "10": 8, "J": 9, "Q": 10, "K": 11, "A": 12}
    cardlist.sort(key=lambda card: sort_order[card.value])
    for card in cardlist:
        if card.value in list(values_present.keys()):
            values_present[card.value] += 1
        else:
            values_present[card.value] = 1
    
    value_check_count = {}
    
    #* Read Pattern *#
    while index+1<len(pattern):
        pattern_check_value = pattern[index+1]
        if pattern_check_value != "0":
            if pattern_check_value in list(value_check_count.keys()):
                value_check_count[pattern_check_value] += 1
            else:
                value_check_count[pattern_check_value] = 1
            
        index += 1
        
        
    #* Check Pattern *#
    
    console.print([str(card) for card in cardlist])
    console.print(values_present)
    console.print(value_check_count)
    is_pattern_valid = True
    
    #* Straight Check Setup *#
    last_card_value = ""
    deck_cardlist_index = 0
    
    for offset_index, (value, count) in enumerate(value_check_count.items()):
        match value:
            case "x" | "y" | "z":
                temp_bool = False
                for key, value in values_present.items():
                    if value >= count:
                        temp_bool = True
                        del values_present[key]
                        break
                is_pattern_valid = False if not temp_bool else is_pattern_valid
            case "a" | "b" | "c" | "d" | "e":
                #* Straight Check *#
                temp_values = deck.values.copy()
                temp_values.append("A")
                temp_card_value = cardlist[offset_index].value
                if last_card_value == "":
                    last_card_value = temp_card_value
                    deck_cardlist_index = temp_values.index(temp_card_value)
                    console.log(deck_cardlist_index)
                else:
                    console.log(f"{deck_cardlist_index} + {offset_index}")
                    if temp_card_value != temp_values[deck_cardlist_index+offset_index]:
                        if temp_card_value == "A" and temp_values[deck_cardlist_index+offset_index] == "6":
                            continue
                        print(f"{temp_card_value} != {temp_values[deck_cardlist_index+offset_index]}")
                        is_pattern_valid = False

    
    #* Flush Check *#
    if pattern_check_suit:
        compare_suit = ""
        for card in cardlist:
            if compare_suit == "":
                compare_suit = card.suit
            else:
                if card.suit != compare_suit:
                    is_pattern_valid = False
    
    return is_pattern_valid