from flask import Blueprint, jsonify, request

from apps.server.wrapper import YtDlpWrapper
from pakcages.schemas.resolve import (
    ErrorResponse,
    ResolveRequest,
    ResolveResponse,
)

api = Blueprint("api", __name__)
wrapper = YtDlpWrapper()


@api.post("/resolve-via-yt-dlp")
def resolve_via_yt_dlp():
    body = request.get_json(silent=True) or {}
    try:
        payload = ResolveRequest(**body)
    except Exception as exc:
        return jsonify(ErrorResponse(error=f"invalid request: {exc}").model_dump()), 400

    try:
        meta = wrapper.resolve_mp3(payload.url)
    except TimeoutError as exc:
        return jsonify(ErrorResponse(error=str(exc)).model_dump()), 504
    except RuntimeError as exc:
        return jsonify(ErrorResponse(error=str(exc)).model_dump()), 502

    response = ResolveResponse(
        title=meta.get("title", ""),
        duration=meta.get("duration"),
        url=meta.get("url", ""),
        webpage_url=meta.get("webpage_url"),
        thumbnail=meta.get("thumbnail"),
        uploader=meta.get("uploader"),
    )
    return jsonify(response.model_dump())
