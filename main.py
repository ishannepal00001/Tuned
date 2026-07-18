from typing import Dict
import sys
import time

from utils import clear_screen

URL_OPTIONS = ["Convert Playlist URL", "Convert Video URL", "Back"]
MENU_OPTIONS = ["Convert URL to .MP3", "Search", "Quit"]


def pretty_print_options(options: list) -> dict:
    options_dict: Dict[int, str] = dict()
    for idx, option in enumerate(options):
        print(f"{idx + 1}: {option}")
        options_dict[idx + 1] = option
    return options_dict


def read_input_safely(prompt: str):
    try:
        inp = str(input(prompt))
        return inp
    except KeyboardInterrupt or EOFError:
        print("\r Exitting the program!....")
        clear_screen()
        sys.exit()


def main():
    print("Welcome to Tuned!")

    while True:
        choices = pretty_print_options(MENU_OPTIONS)
        choice = int(read_input_safely("Choose menu option:"))
        if choice in choices.keys() and choice != max(choices.keys()):
            print(f"You chose {choices[choice]}")
        elif choice == max(choices.keys()):
            print("Exitting the program!")
            clear_screen()
            sys.exit()
        else:
            print("Invalid Option! Try Again")
        while True:
            url_choices = pretty_print_options(URL_OPTIONS)
            url_choice = int(read_input_safely("Choose URL option:"))
            if url_choice in url_choices.keys() and choice != max(url_choices.keys()):
                print(f"You chose {url_choices[choice]}")
            elif choice == max(choices.keys()):
                print("Going Back to the main menu...")
                break
            else:
                print("Invalid Option")


if __name__ == "__main__":
    main()
