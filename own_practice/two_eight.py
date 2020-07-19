"""
程式設計練習題 2.2-2.10 2.8 計算能量.

請撰寫一程式，計算從起始溫度到最後溫度時熱水所需的能量。程式提示使用者數入多少公斤的水、起始溫度
及最後溫度。計算能量的公式如下:

Q = M * (finalTemperature - initialTemperature) * 4184

此處的M逝水的公斤數，溫度是攝氏溫度，而Q是以焦耳(joules)來衡量的能量。
以下是範例輸出的樣本:

```
Enter the amount of water in kilograms: 55.5
Enter the initial temperature: 3.5
Enter the final Temperature:10.5
The energy needed is 1625484.0
```
"""
import ast

M = ast.literal_eval(input("Enter the amount of water in kilograms:"))
initialTemperature = ast.literal_eval(input("Enter the initial temperature:"))
finalTemperature = ast.literal_eval(input("Enter the final Temperature:"))
Q = M * (finalTemperature - initialTemperature) * 4184

print("The energy needed is", Q)
