from argparse import ArgumentParser
from tuned.config import settings
import subprocess
import sys


def do_update():
    result = subprocess.run(
        ["pipx", "upgrade", "tuned"], capture_output=True, text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)


def build_parser():

    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest="commands")
    """System Command Subparser"""
    system_subparser = subparsers.add_parser(
        "update", help="Fetches latest patches or updates for tuned!"
    )
    system_subparser.add_argument(
        "--v",
        "--version",
        help="Specific version to update or mount!",
    )

    """Download Command Subparser"""
    download_parser = subparsers.add_parser("download", help="Downloads a single Video")
    download_parser.add_argument("url", help="URL for the Video to be downloaded.")
    download_parser.add_argument(
        "-fmt",
        "--format",
        help="Download Format for the Video",
        choices=["mp3", "mp4"],
        default="mp3",
    )
    download_parser.add_argument(
        "-o", "--output", default=settings.OUTPUT_DIR, type=str
    )

    """Playlist Download Command Parser"""
    playlist_parser = subparsers.add_parser(
        "playlist", help="Downloads an entire playlist"
    )
    playlist_parser.add_argument("url", help="Playlist URL")
    playlist_parser.add_argument(
        "-fmt",
        "--format",
        help="Download Format for the video",
        choices=["mp3", "mp4"],
        default="mp3",
    )
    playlist_parser.add_argument(
        "-r",
        "--range",
        help="Downloads the video upto the given range.",
        type=int,
        default=None,
    )
    playlist_parser.add_argument(
        "-o",
        "--output",
        help="Downloads the files to the defined directory",
        type=str,
        default=settings.OUTPUT_DIR,
    )
    return parser


def dispatch_args(args, client):
    if args.commands == "download":
        result = client.download_mp3_video(
            url=args.url, output_dir=args.output, codec=args.format
        )
        print(result)
    if args.commands == "update":
        do_update()
