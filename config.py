class Config:
    def __init__(self) -> None:
        self.MENU_OPTIONS = ["Convert URL to .MP3", "Search", "Quit"]
        self.URL_OPTIONS = {
            "convert_video_url_to_mp3": "Convert Video URL",
            "convert_playlist_url": "Convert Playlist URL",
            "Quit": "Quit",
        }


settings = Config()
