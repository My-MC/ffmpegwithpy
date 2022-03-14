import ffmpegwithpy

def test_ffmpeg_01():
    assert ffmpegwithpy.ffmpeg("a.mp4", "mp3").getfilename() == "a.mp3"

def test_ffmpeg_02():
    assert ffmpegwithpy.ffmpeg("a.webm", "mp4").getfilename() == "a.mp4"