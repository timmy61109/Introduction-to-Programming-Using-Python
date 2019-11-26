"""
程式設計練習題 3.3-3.6 3.11 反轉數字.

請撰寫一程式，提示使用者輸入四位數的整數，然後以反轉的順序加以印出，以下是程式輸出的樣本:

```
Enter an integer:1325
The reversed number is 5213
```
"""
# Receive the amount
number = int(input("Enter employee's name:"))


Thousands = str(number // 1000)
number %= 1000
Hundreds = str(number // 100)
number %= 100
Tens = str(number // 10)
number %= 10
Each = str(number // 1)

print(Each + Tens + Hundreds + Thousands)
