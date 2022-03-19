import urllib.request
import shutil
import os
from distutils.dir_util import copy_tree

def main():
    url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n5.0-latest-win64-lgpl-5.0.zip"
    save_name = "FFmpeg.zip"
    os.mkdir("cache")
    urllib.request.urlretrieve(url, save_name)
    shutil.unpack_archive(save_name, "cache")
    copy_tree("./cache/ffmpeg-n5.0-latest-win64-lgpl-5.0/bin", "./")
    shutil.rmtree("./cache")
    os.remove(save_name)

if __name__ == "__main__":
    main()