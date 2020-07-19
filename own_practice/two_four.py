"""
程式設計練習題 2.2-2.10 2.4 將英鎊轉成公斤.

請撰寫一程式，將英鎊轉成公斤。此程式會提示使用者數入英鎊數值，將英鎊轉換成公斤後顯示期結果。1英
鎊等於0.454公斤。所以是範例輸出樣本:
```
Enter a value in pounds:55.5
55.5 pounds is 25.197 kilograms
```
"""
import ast


feet = ast.literal_eval(input("Enter a value in pounds:"))

meters = feet * 0.454

print(feet, 'pounds is', meters, "kilograms")
