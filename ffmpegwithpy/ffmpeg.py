"""Run FFmpeg

This module runs FFmpeg based on the input and performs file conversion and encoding.

Todo:
    * Cover all arguments
"""

import subprocess
from typing import Dict, Optional


def get_filename(filepath: str, file_format: str) -> str:
    filename = filepath.split(".")[0]
    return f"{filename}.{file_format}"


def parse_options(options: Dict[str, int]) -> str:
    option_map = []

    if "qv" in options:
        val = options.get("qv")
        option_map.append(f"-q:v {val}")

    if "ab" in options:
        val = options.get("ab")
        option_map.append(f"-ab {val}")

    option_arg = ""

    for i in option_map:
        option_arg += f" {i}"

    return option_arg


def _ffmpeg_cmd(filepath: str, file_format: str, options: Optional[Dict[str, int]] = None) -> str:
    if options:
        option_arg = parse_options(options)
    else:
        option_arg = ""

    after_filename = get_filename(filepath, file_format)
    return f"ffmpeg -y -i {filepath}{option_arg} {after_filename}"


class FFmpeg:
    """Class that executes FFmpeg and processes files

    Args:
        arg1(str): File name of the source file to be converted
        arg2(str): Extension to be converted
        opt(optional): Option
    """

    def __init__(self, filepath: str, file_format: str, options: Optional[Dict[str, int]] = None):
        self.filepath = filepath
        self.file_format = file_format
        self.options = options

    def ffmpeg_cmd(self) -> str:
        if self.options is not None:
            cmd = _ffmpeg_cmd(self.filepath, self.file_format, self.options)
        else:
            cmd = _ffmpeg_cmd(self.filepath, self.file_format, None)

        return cmd

    def ffmpeg(self) -> None:
        """Function to write cmd to convert with FFmpeg and have it run"""

        if self.options:
            cmd = _ffmpeg_cmd(self.filepath, self.file_format, self.options)
        else:
            cmd = _ffmpeg_cmd(self.filepath, self.file_format, None)

        subprocess.run(cmd, shell=True)
