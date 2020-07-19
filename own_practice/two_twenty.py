"""
程式設計練習題 2.2-2.10 2.20 財務金融應用程式:計算利息.

利息公式:

interest = balance * (annualInterestRate / 1200)

以下是輸出樣本:
```
Enter balance and interest rate (e.g., 3 for 3%):1000, 3.5
The interest is 1043.33
```
"""
import ast


balance, annualInterestRate = ast.literal_eval(
    input("Enter investment amount:"))

interest = balance * (annualInterestRate / 1200)

print("The interest is", interest)
