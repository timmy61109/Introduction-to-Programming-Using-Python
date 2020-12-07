"""
程式設計練習題 2.2-2.10 2.10 物理學:找出跑到長度.

請撰寫一程式，找出跑道長度，公式如下:

v 飛機的速度m/s
a 飛機的加速度m/s^2

length = v ** 2 / 2 * a

以下是範例輸出樣本:
```
Enter speed and acceleration: 60, 3.5
The minimum runway length for this airplane is 514.286 meters
```
"""
import ast


v, a = ast.literal_eval(input("Enter speed and acceleration:"))
length =  v ** 2 / (2 * a)

print("The wind chill index is", length, "meters")
