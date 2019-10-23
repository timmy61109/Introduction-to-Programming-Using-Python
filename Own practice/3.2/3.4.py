"""
程式設計練習題 2.2-2.10 3.4 幾何:五邊形面積.

計算五邊形(pentagon)面積的公式(s表示邊長)為:

Area = (5 * tan(54)) / 4 * s ** 2

提示使用者輸入邊長，接著顯示其面積，以下是程式的執行結果:
```
Enter the side:5.5
The area of the pentagon is 52.04444136781625
```
"""
import math


s = eval(
    input("Enter the side:"))

area = (5 * math.tan(math.radians(54))) / 4 * s ** 2

print("The area of the pentagon is", area)
