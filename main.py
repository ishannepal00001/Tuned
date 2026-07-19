from typing import Dict
import sys
import time

from utils import clear_screen

URL_OPTIONS = {
    "convert_video_url_to_mp3": "Convert Video URL",
    "convert_playlist_url": "Convert Playlist URL",
    "Quit": "Quit",
}
MENU_OPTIONS = ["Convert URL to .MP3", "Search", "Quit"]


def pretty_print_options(options: Dict[str, str] | list) -> dict:
    options_dict = (
        {
            int(idx + 1): (function_key, display_value)
            for idx, (function_key, display_value) in enumerate(options.items())
        }
        if isinstance(options, dict)
        else {int(idx + 1): value for idx, value in enumerate(options)}
    )
    return options_dict


def read_input_safely(prompt: str, type_conv):
    try:
        inp = str(input(prompt))
        return type_conv(inp)
    except KeyboardInterrupt, EOFError:
        print("\r Exitting the program!....")
        clear_screen()
        sys.exit()
    except ValueError:
        print("\n Unexpected Value Type")
        sys.exit()


def main():
    print("Welcome to Tuned!")

    while True:
        choices = pretty_print_options(MENU_OPTIONS)
        choice = read_input_safely("Choose menu option:", type_conv=int)
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
            url_choice = read_input_safely("Choose URL option:", type_conv=int)
            if url_choice in url_choices.keys() and choice != max(url_choices.keys()):
                print(f"You chose {url_choices[choice]}")
            elif choice == max(choices.keys()):
                print("Going Back to the main menu...")
                break
            else:
                print("Invalid Option")


if __name__ == "__main__":
    main()
