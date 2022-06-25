"""Return command or filename

This module returns the command and filename when FFmpeg is run.

Todo:
    * Add a function that retrieves data from FFprobe and returns it.
"""

from typing import Optional

from pydantic import BaseModel


class get:
    """Class for obtaining information about ffmpeg

    Args:
        arg1(str): File name of the source file to be converted
        arg2(str): Extension to be converted
        opt(optional): Option
    """

    class Options(BaseModel):
        qv: Optional[int]
        ab: Optional[int]

    def __init__(self, arg1: str, arg2: str, opt: Optional[Options] = None):
        self.arg1 = arg1
        self.arg2 = arg2
        self.opt = opt

    def getfilename(self) -> str:
        """Function to return the name of the converted file"""
        name = self.arg1.split(".")[0]
        aname = f"{name}.{self.arg2}"
        return aname

    def getcommand(self) -> str:

        name = self.arg1.split(".")[0]
        aname = f"{name}.{self.arg2}"

        if self.opt:
            if self.opt.qv is None:
                qv = ""
            else:
                qv = f"-q:v {self.opt.qv}"

            if self.opt.ab is None:
                ab = ""
            else:
                ab = f"-ab {self.opt.ab}"

            cmd = f"ffmpeg -y -i {self.arg1} {qv} {ab} {aname}"
        else:
            cmd = f"ffmpeg -y -i {self.arg1} {aname}"

        return cmd
