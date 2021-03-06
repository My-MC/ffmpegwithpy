import ffmpegwithpy


def test_ffmpeg_01():
    assert ffmpegwithpy.get("getfilename01.mp4", "mp3").getfilename() == "getfilename01.mp3"


def test_ffmpeg_02():
    assert ffmpegwithpy.get("getfilename02.webm", "mp4").getfilename() == "getfilename02.mp4"


def test_getcommand_01():
    assert ffmpegwithpy.get("getcommand01.mp4", "mp3").getcommand() == "ffmpeg -y -i getcommand01.mp4 getcommand01.mp3"


def test_getcommand_02():
    ffmpeg_opt = {"qv": "1"}
    opt = ffmpegwithpy.get.Options(**ffmpeg_opt)

    assert (
        ffmpegwithpy.get("getcommand02.mp4", "mp3", opt).getcommand()
        == "ffmpeg -y -i getcommand02.mp4 -q:v 1  getcommand02.mp3"
    )


def test_getcommand_03():
    ffmpeg_opt = {"qv": "12"}
    opt = ffmpegwithpy.get.Options(**ffmpeg_opt)

    assert (
        ffmpegwithpy.get("getcommand03.mp4", "mp3", opt).getcommand()
        == "ffmpeg -y -i getcommand03.mp4 -q:v 12  getcommand03.mp3"
    )


def test_getcommand_04():
    ffmpeg_opt = {"qv": "12", "ab": "192"}
    opt = ffmpegwithpy.get.Options(**ffmpeg_opt)

    assert (
        ffmpegwithpy.get("getcommand03.mp4", "mp3", opt).getcommand()
        == "ffmpeg -y -i getcommand03.mp4 -q:v 12 -ab 192 getcommand03.mp3"
    )
