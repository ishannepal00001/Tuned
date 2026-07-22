from argparse import ArgumentParser, Namespace
from main import settings


def build_parser():

    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest="commands")
    parser.add_argument("-h", "--help", help="Shows all Argument for the CLI")

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
    if args.command == "download":
        result = client.download_mp3_video(
            url=args.url, output_dir=args.output, codec=args.codec
        )
        print(result)
