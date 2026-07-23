from tuned.utils import clear_screen, pretty_print_options, read_input_safely
from tuned.config import settings

import sys

MENU_OPTIONS = settings.MENU_OPTIONS
URL_OPTIONS = settings.URL_OPTIONS


def run_repl():
    while True:
        pretty_print_options(MENU_OPTIONS)
        choice = read_input_safely("Choose menu option:", type_conv=int)
        if choice == len(MENU_OPTIONS):
            print("Exitting the Program")
            clear_screen()
            sys.exit()
        elif choice > len(MENU_OPTIONS):
            print("Invalid Option!")
        else:
            print(f"You chose {MENU_OPTIONS[choice]}")
        while True:
            pretty_print_options(URL_OPTIONS)
            url_choice = read_input_safely("Choose URL option:", type_conv=int)
            if url_choice in URL_OPTIONS.keys() and choice != max(URL_OPTIONS.keys()):
                print(f"You chose {list(URL_OPTIONS)[url_choice]}")
            elif choice == max(URL_OPTIONS.keys()):
                print("Going Back to the main menu...")
                break
            else:
                print("Invalid Option")


if __name__ == "__main__":
    run_repl()
