"""
程式設計練習題 2.2-2.10 2.3 將英吋轉換成公尺.

請撰寫一程式，讀取英吋(feet)數，將期轉換為公尺(meter)，秉顯示結果。一英吋相當於.0.305公尺。以
下是範例輸出樣本:
```
Enter a value for feet:16.5
16.5 feet is 5.0325 meters
```
"""
import ast
feet = ast.literal_eval(input("Enter a value for feet:"))

meters = feet * 0.305

print(feet, 'feet is', meters, "meters")
