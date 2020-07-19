"""
程式設計練習題 2.2-2.10 2.21 財務金融應用程式:複利值.

利息公式:

100 * (1 + 0.00417) = 100.417
(100 + 100.417) * (1 + 0.00417) = 201.252
(100 + 201.252) * (1 + 0.00417) = 302.507

以下是輸出樣本:
```
Enter the monthly saving amount:100
After the sixth month, the account value is 608.81
```
"""
import ast


amount = ast.literal_eval(input("Enter the monthly saving amount:"))

account_value = amount
amount *= (1 + 0.00417)

amount = amount + account_value
amount *= (1 + 0.00417)

amount = amount + account_value
amount *= (1 + 0.00417)

amount = amount + account_value
amount *= (1 + 0.00417)

amount = amount + account_value
amount *= (1 + 0.00417)

amount = amount + account_value
amount *= (1 + 0.00417)

print("After the sixth month, the account value is", amount)
