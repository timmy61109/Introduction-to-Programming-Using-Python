"""
程式設計練習題 2.2-2.10 2.13 分割數字.

請撰寫一程式提示使用者數入四位數的整數，然後以反轉順序顯示。以下是範例輸出樣本:
```
Enter an integer:5213
3
1
2
5
```
"""

integer = eval(input("Enter an integer:"))

print(integer % 10)
integer //= 10

print(integer % 10)
integer //= 10

print(integer % 10)
integer //= 10

print(integer % 10)
integer //= 10
