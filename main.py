from cli.parser import dispatch_args
from cli.repl import run_repl
from config import Config
from utils import args_parser
import sys

from cli.downloader import Downloader

client = Downloader()
settings = Config()


def main():
    command_args = sys.argv[:1]
    if command_args is None:
        run_repl()

    args = args_parser(command_args)
    dispatch_args(args, client)

    print("Hello from Tuned!")


if __name__ == "__main__":
    main()
