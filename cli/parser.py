from argparse import ArgumentParser, Namespace

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

"""Playlist Download Command Parser"""
playlist_parser = subparsers.add_parser("playlist", help="Downloads an entire playlist")
playlist_parser.add_argument("url", help="Playlist URL")
playlist_parser.add_argument(
    "-fmt",
    "--format",
    help="Download Format for the video",
    choices=["mp3", "mp4"],
    default="mp3",
)
