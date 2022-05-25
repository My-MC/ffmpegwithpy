"""ffmpegのコマンド"""

import subprocess


class ffmpeg:
    """ffmpegを実行しファイルを処理するクラス

    Args:
        arg1(str): 変換元のファイル名
        arg2(str): 変換したい拡張子
        qv(int, optional): 変換したいビデオのクオリティー(ビデオのときのみ有効)
        ab(int, optional): 変換するもののオーディオのビットレート
    """

    def __init__(self, arg1, arg2, qv=None, ab=None):
        self.arg1 = arg1
        self.arg2 = arg2
        self.qv = qv
        self.ab = ab

    def ffmpeg(self):
        """ffmpegで変換するためにcmdを書いてそれを実行させる"""

        name = self.arg1.split(".")[0]
        aname = f"{name}" + "." + str(self.arg2)

        if self.qv == None:
            qv = ""
        else:
            qv = f"-q:v {self.qv}"

        if self.ab == None:
            ab = ""
        else:
            ab = f"-ab {self.ab}"
        cmd = f"ffmpeg -y -i {self.arg1} {qv} {ab} {aname}"

        subprocess.run(cmd, shell=True)
