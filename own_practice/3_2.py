"""
程式設計練習題 2.2-2.10 3.2 幾何:大圓距離.

撰寫一程式提示使用者輸入球面上兩點，並計算出這兩點間在圓表面的最短距離。
地球半徑平均6371.01km。

d = radius * acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))

以下是程式的執行結果:
```
Enter point 1 (latitude and longitude) in degrees:
39.55, -116.25
Enter point 2 (latitude and longitude) in degrees:
41.5, 87.37
The distance between the two points is 10691.79183231593 km
```
"""
import math


radius = 6371.01
x1, y1 = eval(
    input("Enter point 1 (latitude and longitude) in degrees:\n"))
x2, y2 = eval(
    input("Enter point 2 (latitude and longitude) in degrees:\n"))

x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

d = radius * math.acos(
    math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(
        y1 - y2))

print("The distance between the two points is", d, "km")
