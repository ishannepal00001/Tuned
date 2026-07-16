from pydantic import BaseModel


class ResolveRequest(BaseModel):
    url: str


class ResolveResponse(BaseModel):
    title: str
    duration: float | None = None
    url: str
    webpage_url: str | None = None
    thumbnail: str | None = None
    uploader: str | None = None


class ErrorResponse(BaseModel):
    error: str
