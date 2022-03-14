"""ffmpegのコマンド"""

import subprocess


class ffmpeg:
    """ "ffmpegで変換するためにcmdを書いてそれを実行させる"""

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def ffmpeg(self):
        """ "
        arg1は変換したいファイル名
        arg2は変換したい拡張子名
        """

        name = self.arg1.split(".")[0]
        aname = f"{name}" + "." + str(self.arg2)

        cmd = f"ffmpeg {self.arg1} {aname}"
        subprocess.run(cmd, shell=True)

    def getfilename(self):
        """変換後のファイル名を返す関数"""
        name = self.arg1.split(".")[0]
        aname = f"{name}" + "." + str(self.arg2)
        return aname


if __name__ == "__main__":
    ffmpeg("a.mp4", "mp3").ffmpeg()
    print(ffmpeg("a.mp4", "mp3").getfilename())
