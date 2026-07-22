import subprocess
import sys
import time
from typing import Dict


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


def clear_screen() -> None:
    time.sleep(0.8)
    subprocess.run(["clear"])


def pretty_print_options(options: Dict[str, str] | list):
    {
        print(f"\n {idx}:{display_option}")
        for idx, (display_option, menu_option) in enumerate(options.items(), start=1)
    } if isinstance(options, dict) else {
        print(f"\n {idx}: {option}") for idx, option in enumerate(options, start=1)
    }


def get_argument_length() -> int:
    length = len(sys.argv)
    return length
