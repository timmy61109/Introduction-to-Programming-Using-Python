"""
程式設計練習題 2.2-2.10 2.15 幾何:正六邊形的面積.

請撰寫一程式提示使用者輸入正六邊形的邊長，然後顯示期面積。計算六邊形面積的公式如下:

area = (3 * (3 ** 0.5) / 2) * s ** 2

以下是輸出樣本:
```
Enter the side:5.5
The area of the hexagon is 78.5895
```
"""
import ast


s = ast.literal_eval(input("Enter the side:"))

area = (3 * (3 ** 0.5) / 2) * s ** 2

print("The area of the hexagon is", area)
