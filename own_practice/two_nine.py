"""
程式設計練習題 2.2-2.10 2.8 科學:風寒效應.

請撰寫一程式，計算風寒效應，公式如下:

twc = 35.74 + 0.6215 * ta - 35.75 * (v ** 0.16) + 0.4275 * ta * (v ** 0.16)

ta 室外測量的華氏溫度
v 英哩/小時
twc 風寒效應的溫度

2 mph < v or 41F ta < -58F
```
Enter the temperature in Fahrenheit between -58 and 41: 5.3
Enter the wind speed in miles per hour: 6
The wind chill index is -5.56707
```
"""

TA = eval(input("Enter the temperature in Fahrenheit between -58 and 41:"))
v = eval(input("Enter the wind speed in miles per hour:"))
twc = 35.74 + 0.6215 * TA - 35.75 * (v ** 0.16) + 0.4275 * TA * (v ** 0.16)

print("The wind chill index is", twc)
