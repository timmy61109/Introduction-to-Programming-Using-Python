"""
程式設計練習題 2.2-2.10 2.2 計算原著的體積.

請撰寫一程式，讀取原著的半徑與長度，在利用以下公式，計算其體積:

area = radius * radius * pi
volume = area * length
"""
import ast


radius, length = ast.literal_eval(
    input("Enter the radius and length of a cylinder:"))

area = radius * radius * 3.141596
volume = area * length

print("The area is", area)
print("The volume is", volume)
