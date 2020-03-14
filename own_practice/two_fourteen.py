u"""
程式設計練習題 2.2-2.10 2.14 幾何:計算三角形的面積.

請撰寫一程式，提示使用者輸入三角形的三點座標(x1, y1)、(x2, y2)以及(x3, y3)，然後顯示期面積。

s = (side1 + side2 + side3) / 2
area = (s * (s - side1)(s - side2)(s - side3)) ** 0.5

以下是輸出樣本:
```
Enter three points for a triangle:1.5, -3.4, 4.6, 5, 9.5, -3.4
The area of the triangle is 33.6
```
"""

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle:"))

side1 = ((x1 - x2) ** 2 + (y1 + y2) ** 2) ** 0.5
side2 = ((x2 - x3) ** 2 + (y2 + y3) ** 2) ** 0.5
side3 = ((x1 - x3) ** 2 + (y1 + y3) ** 2) ** 0.5

s = (side1 + side2 + side3) / 2
AREA = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

print(AREA)
