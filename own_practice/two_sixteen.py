"""
程式設計練習題 2.2-2.10 2.16 物理:加速度.

平均加速度為兩個速度之差，除以時間。計算公式如下:
v0 = 起始速度
v1 = 結束速度
t = 所花的時間

a = (v1 - v0) / t

以下是輸出樣本:
```
Enter the side:5.5, 50.9, 4.5
The area of the hexagon is 10.088888888888889
```
"""
import ast


v0, v1, t = ast.literal_eval(input("Enter v0, v1 and t:"))

a = (v1 - v0) / t

print("The area of the hexagon is", a)
