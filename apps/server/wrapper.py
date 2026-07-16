import json
import subprocess
from typing import Any

from pakcages.core.settings import settings


class YtDlpWrapper:
    def __init__(
        self,
        timeout: int | None = None,
        player_client: str | None = None,
    ) -> None:
        self.timeout = timeout if timeout is not None else settings.yt_dlp_timeout
        self.player_client = (
            player_client if player_client is not None else settings.yt_dlp_player_client
        )

    def _build_base_args(self) -> list[str]:
        return [
            "yt-dlp",
            "-j",
            "--skip-download",
            "-f",
            "bestaudio",
            "--extractor-args",
            f"youtube:player_client={self.player_client}",
        ]

    def resolve_mp3(self, url: str) -> dict[str, Any]:
        args = self._build_base_args() + [url]
        try:
            proc = subprocess.run(
                args,
                capture_output=True,
                text=True,
                timeout=self.timeout,
                check=True,
            )
        except subprocess.TimeoutExpired as exc:
            raise TimeoutError(
                f"yt-dlp timed out after {self.timeout}s resolving {url}"
            ) from exc
        except subprocess.CalledProcessError as exc:
            raise RuntimeError(
                f"yt-dlp failed: {exc.stderr.strip() or exc.stdout.strip()}"
            ) from exc
        return json.loads(proc.stdout)

    def download_mp3(self, url: str, output_path: str) -> dict[str, Any]:
        args = self._build_base_args()[:]
        args += [
            "-x",
            "--audio-format",
            "mp3",
            "-o",
            output_path,
            url,
        ]
        try:
            proc = subprocess.run(
                args,
                capture_output=True,
                text=True,
                timeout=self.timeout,
                check=True,
            )
        except subprocess.TimeoutExpired as exc:
            raise TimeoutError(
                f"yt-dlp timed out after {self.timeout}s downloading {url}"
            ) from exc
        except subprocess.CalledProcessError as exc:
            raise RuntimeError(
                f"yt-dlp failed: {exc.stderr.strip() or exc.stdout.strip()}"
            ) from exc
        return json.loads(proc.stdout)
