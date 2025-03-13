from typing import Any, Dict
from .deck import CardList
from rich.console import Console

def _remove_from_dict(_value: Any, _dict: Dict[Any, Any]) -> None:
    for key, value in _dict.items():
        if value == _value:
            del _dict[key]
            return

def check(cardlist: CardList, pattern: str) -> bool:
    console = Console()
    index = 0
    pattern_check_suit = pattern[0] == "1"
    values_present = {}
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
            
        index += 2
    #* Check Pattern *#
    console.print(values_present)
    console.print(value_check_count)
    is_pattern_valid = True
    for value, count in value_check_count.items():
        match value:
            case "x" | "y" | "z":
                if count in list(values_present.values()):
                    _remove_from_dict(count, values_present)
                else:
                    is_pattern_valid = False
    
    return is_pattern_valid