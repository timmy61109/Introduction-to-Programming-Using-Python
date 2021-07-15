"""YouTube Speech recognition.

將YouTube影片自動化辨識影片內容並輸出語詞內容。(英文)
"""
from __future__ import unicode_literals
from os import listdir
import speech_recognition as sr
import youtube_dl

URL = str(input("Enter your url: "))
PATH = "./"


class MyLogger(object):
    """."""

    def debug(self, msg):
        """."""
        pass

    def warning(self, msg):
        """."""
        pass

    def error(self, msg):
        """."""
        print(msg)


def my_hook(d):
    """."""
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '320',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL])
    files = listdir(PATH)
    r = sr.Recognizer()  # 預設辨識英文
    for file in files:
        if file[-4:] == '.wav':
            print(file)
            with sr.WavFile(file) as source:
                audio = r.record(source)
            try:
                print("Transcription: " + r.recognize_sphinx(audio))
                # 使用CMU Sphinx的服務
            except LookupError:
                print("Could not understand audio")
