"""
程式設計練習題 2.2-2.10 2.6 將一整數的每位數加總.

請撰寫一程式，讀取0到1000其中一個整數，將一整數的每位數加總。比方說，雅社讀取的整數為932，則此
數的每位數之總和為14(提示:使用%運算子取出所有位數，使用//運算子移除取出的數位。例如，
932 % 10 = 2，932 // 10 = 93。)以下是範例輸出樣本:
```
Enter a number between 0 and 1000:999
The sum of digits is 18.04
```
"""

number = eval(input("Enter a number between 0 and 1000:"))

number_digits = number % 10
number = number // 10
ten_digits = number % 10
number = number // 10
hundreds_digit = number % 10
number = number // 10
thousand_digits = number % 10

total = number_digits + ten_digits + hundreds_digit + thousand_digits

print("The sum of digits is", total)
