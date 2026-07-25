from typing import Any, Dict
from yt_dlp import YoutubeDL


class Downloader:
    def _build_opts(
        self,
        output_dir: str,
        codec: str = "mp3",
        quality: str = "0",
        embed_thumbnail: bool = True,
    ) -> Dict[str, Any]:
        opts = {
            "format": "bestaudio/best",
            "extractaudio": True,
            "audioformat": codec,
            "audioquality": quality,
            "addmetadata": True,
            "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        }
        opts["embed_thumbnail"] = embed_thumbnail if embed_thumbnail else ...
        return opts

    def download_mp3_video(
        self,
        url: str,
        output_dir: str,
        codec: str = "mp3",
        embed_thumbnail: bool = True,
    ):
        opts = self._build_opts(
            output_dir=output_dir, codec=codec, embed_thumbnail=embed_thumbnail
        )
        opts["noplaylist"] = True
        try:
            with YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
        except Exception as e:
            return None
        return info
