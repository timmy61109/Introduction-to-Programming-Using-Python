"""
程式設計練習題 2.2-2.10 3.7 隨機字元.

請撰寫一程式，使用time.time()函式顯示隨機的大寫字母:
"""

import time


time_number = int(time.time())

character = chr(int(time_number % 100))

print("隨機的大寫字母", character)
