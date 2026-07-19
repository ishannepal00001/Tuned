import subprocess
import sys
import time


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
