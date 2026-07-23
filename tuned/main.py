from argparse import Namespace
from tuned.cli.parser import dispatch_args
from tuned.cli.repl import run_repl
from tuned.utils import args_parser
import sys

from tuned.cli.downloader import Downloader

client = Downloader()


def main():
    command_args = sys.argv[1:]
    if not command_args:
        run_repl()
    args: Namespace = args_parser(command_args)
    dispatch_args(args, client)

    print("Hello from Tuned!")


if __name__ == "__main__":
    main()
