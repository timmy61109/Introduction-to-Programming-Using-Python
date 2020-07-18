"""
程式設計練習題 2.2-2.10 2.17 健康累應用程式:計算IBM.

身高的平方除以體重。計算公式如下:

m ** 2 / h

以下是輸出樣本:
```
Enter weight in pounds:95.5
Enter height in inches:50
BMI is 26.8573
```
"""
import ast


weight = ast.literal_eval(input("Enter weight in pounds:"))
height = ast.literal_eval(input("Enter height in inches:"))

weight *= 0.45359237
height *= 0.0254
bmi = weight / (height ** 2)

print("BMI is", bmi)
