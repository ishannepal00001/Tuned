from textual.widgets import Input
from textual.app import ComposeResult


class URLBar(Input):
    """A search/URL input bar that accepts keywords or URLs."""

    def __init__(self, placeholder: str = "Search or enter URL...", **kwargs) -> None:
        super().__init__(placeholder=placeholder, **kwargs)
