"""ffmpegwithpy

This package is a wrapper for FFmpeg that runs FFmpeg from Python.

Todo:
    * Cover all arguments
    * Cover FFprobe
    * Cover FFplay
"""

from .ffmpeg import FFmpeg, get_filename, parse_options

__version__ = "0.1.0"

__all__ = ["FFmpeg", "get_filename", "parse_options"]
