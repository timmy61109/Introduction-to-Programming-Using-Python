"""
程式設計練習題 2.2-2.10 2.1 將攝氏溫度轉換成華氏溫度.

請撰寫一程式，從控制臺讀取攝氏溫度，接著將其轉換為華氏溫度，並顯示結果。轉換的公式如下:
fahrenheit = (9 / 5) * celsius + 32
"""

celsius = eval(input("Enter a degree in Celsius:"))

fahrenheit = (9 / 5) * celsius + 32

print(celsius, "Celsius is", fahrenheit, "Fahrenheit")
