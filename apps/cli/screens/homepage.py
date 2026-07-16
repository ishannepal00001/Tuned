from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Header, Footer, Input, Static, Button
from textual.containers import Vertical, Horizontal, Center
from textual.reactive import reactive

from apps.cli.widgets.ascii_title import AsciiTitle
from apps.cli.widgets.url_bar import URLBar


class Homepage(Screen):
    """Homepage with search bar for keywords or URLs."""

    BINDINGS = [
        ("escape", "app.pop_screen", "Back"),
    ]

    search_query = reactive("")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Center(
                AsciiTitle(),
                id="title-container",
            ),
            Center(
                Static("Search for music, podcasts, or enter a URL", id="subtitle"),
                id="subtitle-container",
            ),
            Center(
                URLBar(id="search-bar"),
                id="search-container",
            ),
            Center(
                Horizontal(
                    Button("Search", id="search-btn", variant="primary"),
                    Button("Clear", id="clear-btn", variant="default"),
                    id="buttons-container",
                ),
                id="buttons-wrapper",
            ),
            Static("By Ishan Nepal", id="credit"),
            id="main-container",
        )
        yield Footer()

    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle input changes in the search bar."""
        self.search_query = event.value

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle search submission via Enter key."""
        self._perform_search(event.value)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "search-btn":
            search_bar = self.query_one("#search-bar", URLBar)
            self._perform_search(search_bar.value)
        elif event.button.id == "clear-btn":
            search_bar = self.query_one("#search-bar", URLBar)
            search_bar.value = ""

    def _perform_search(self, query: str) -> None:
        """Execute the search with the given query."""
        if not query.strip():
            return

        self.search_query = query

        if self._is_url(query):
            self.notify(f"Opening URL: {query}", severity="information")
        else:
            self.notify(f"Searching for: {query}", severity="information")

    def _is_url(self, text: str) -> bool:
        """Check if the input text is a URL."""
        url_indicators = ["http://", "https://", "www.", ".com", ".org", ".net", ".io"]
        text_lower = text.lower().strip()
        return any(indicator in text_lower for indicator in url_indicators)
