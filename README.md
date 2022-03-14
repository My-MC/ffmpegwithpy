# ffmpegwithpy

## About

This library is Python FFmpeg wrapper.

We would like to be able to add all FFmpeg features in the future!

## How to use

ffmpeg

Convert files

arg1 = Name before conversion

arg2 = Name of extension to be converted

Example

``` python
import ffmpegwithpy
filename = ffmpegwithpy.ffmpeg("a.mp4", "mp3")
filename.ffmpeg()
# or
ffmpegwithpy.ffmpeg("a.mp4", "mp3").ffmpeg()
```

getfilename

Returns the converted name

Example

``` python
import ffmpegwithpy
filename = ffmpegwithpy.ffmpeg("a.mp4", "mp3")
print(filename.getfilename())
# or
print(ffmpegwithpy.ffmpeg("a.mp4", "mp3").ffmpeg())
```
