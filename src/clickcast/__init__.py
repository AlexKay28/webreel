"""clickcast — drive a browser, return a reel + AI-readable feedback sidecar."""

from importlib.metadata import PackageNotFoundError, version

from clickcast.reel import AsyncReel, Reel, discover

try:
    __version__ = version("clickcast")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"

__all__ = ["AsyncReel", "Reel", "__version__", "discover"]
