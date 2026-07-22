from cli.repl import run_repl
from utils import get_argument_length


def main():
    args = get_argument_length()
    if args == 1:
        run_repl()
        return

    print("Hello from Tuned!")


if __name__ == "__main__":
    main()
