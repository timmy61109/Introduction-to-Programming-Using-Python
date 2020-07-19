"""
程式設計練習題 3.3-3.6 3.11 反轉數字.

請撰寫一程式，提示使用者輸入四位數的整數，然後以反轉的順序加以印出，以下是程式輸出的樣本:

```
Enter an integer:1325
The reversed number is 5213
```
"""
# Receive the amount
NUMBER = int(input("Enter employee's name:"))

THOUSANDS = str(NUMBER // 1000)
NUMBER %= 1000
HUNDREDS = str(NUMBER // 100)
NUMBER %= 100
TENS = str(NUMBER // 10)
NUMBER %= 10
EACH = str(NUMBER // 1)

print(EACH + TENS + HUNDREDS + THOUSANDS)
