"""
程式設計練習題 2.2-2.10 3.5 幾何:n多邊形面積.

正多邊行為帶有n個邊、各邊等長、各角度也相同的正多邊形，計算正多邊形面積的公式:

Area = (n * tan(pi / n)) / 4 * s ** 2

提示使用者輸入邊長，接著顯示其面積，以下是程式的執行結果:
```
Enter the side:5.5
The area of the pentagon is 52.04444136781625
```
"""
import math


n = eval(input("Enter the number of side:"))
s = eval(input("Enter the side:"))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print("The area of the pentagon is", area)
