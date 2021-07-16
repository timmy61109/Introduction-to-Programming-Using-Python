"""Traditional Chinese speech recognition.

將低於10秒的語音進行語音辨識並輸出語詞內容。(中文)
"""
import speech_recognition as sr

r = sr.Recognizer()
with sr.WavFile("c9DxQmY.wav") as source:
    audio = r.record(source)
try:
    print(
        "Transcription: " + r.recognize_google(
            audio, language='zh-TW'))
    # 使用CMU Sphinx的服務
except LookupError:
    print("Could not understand audio")
