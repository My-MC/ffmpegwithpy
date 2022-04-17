# ffmpegwithpy

## About

This library is Python FFmpeg wrapper.

We would like to be able to add all FFmpeg features in the future!

## How to use

### ffmpeg

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

### getfilename

Returns the converted name

Example

``` python
import ffmpegwithpy
filename = ffmpegwithpy.get("a.mp4", "mp3")
print(filename.getfilename())
# or
print(ffmpegwithpy.get("a.mp4", "mp3").getfilename())
```

### getcommand

Returns the command

Example

``` python
import ffmpegwithpy
filename = ffmpegwithpy.get("a.mp4", "mp3")
print(filename.getcommand())
# or
print(ffmpegwithpy.get("a.mp4", "mp3").getcommand())
```

## Developing

### Installation of Development Environment

This library uses [Poetry](https://python-poetry.org). So the installation of the development environment will be the following command.

``` bash
poetry install
# Entering the virtual environment
poetry shell
```

### Code

This library uses black and isort as code formatters. Use the following command to execute.

``` bash
black .
isort .
```
