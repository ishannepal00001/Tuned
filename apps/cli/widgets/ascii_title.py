import pyfiglet
from textual.widgets import Static


class AsciiTitle(Static):
    """A title widget that renders text as ASCII art using pyfiglet."""

    def __init__(self, text: str = "Tuned", font: str = "standard", **kwargs) -> None:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        super().__init__(ascii_art, **kwargs)
