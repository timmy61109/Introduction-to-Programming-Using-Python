"""
程式設計練習題 2.2-2.10 3.1 幾何:五邊形的面積.

撰寫一程式提示使用者輸入從五邊形(pentagon)的中心到頂點(vertex)的長度，然後計算五邊形的面積。

s = 2 * r * sin(pi / 5)
Area = (5 * tan(54)) / 4 * s ** 2

四捨五入到小數點後兩位，以下是程式的執行結果:
```
Enter the length from the center to a vertex:5.5
The area of the pentagon is 71.92
```
"""
import ast

import math


r = ast.literal_eval(
    input("Enter the length from the center to a vertex:"))

s = 2 * r * math.sin(math.radians(36))
Area = (5 * math.tan(math.radians(54))) / 4 * s ** 2

print("The area of the pentagon is", format(Area, ".2f"))
