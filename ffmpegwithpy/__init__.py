"""ffmpegwithpy

This package is a wrapper for FFmpeg that runs FFmpeg from Python.

Todo:
    * Cover all arguments
    * Cover FFprobe
    * Cover FFplay
"""

from .ffmpeg import ffmpeg
from .get import get

__version__ = "0.1.1"

__all__ = ["ffmpeg", "get"]
