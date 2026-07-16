from textual.app import App, ComposeResult
from textual.binding import Binding

from apps.cli.screens.homepage import Homepage


class TunedApp(App):
    """Main CLI application for Tuned."""

    TITLE = "Tuned"
    SUB_TITLE = "Music & Podcast Search"

    CSS_PATH = [
        "../../pakcages/core/styles/index.tcss",
        "screens/homepage.tcss",
        "widgets/ascii_title.tcss",
        "widgets/url_bar.tcss",
    ]

    BINDINGS = [
        Binding("q", "quit", "Quit"),
    ]

    def on_mount(self) -> None:
        """Push the homepage screen on startup."""
        self.push_screen(Homepage())


def main():
    app = TunedApp()
    app.run()


if __name__ == "__main__":
    main()
