from typing import Any, Dict


def generic_cli(menu: Dict[str, Dict[str, Any]]):
    start_message = (f'{key} - {value["message"]}' for key, value in menu.items())
    menu_text = "\n".join(start_message)

    choice = input(f"\nEnter your choice:\n{menu_text}\n")
    while choice not in menu:  
        if choice not in menu:
            choice = input(f"\nEnter your choice:\n{menu_text}\n")
            print("\nInvalid choice")

    menu[choice]["func"]()
