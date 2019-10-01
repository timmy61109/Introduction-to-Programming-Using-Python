"""
程式設計練習題 2.2-2.10 2.19 財務金融應用程式:計算未來投資價值.

計算未來投資價值公式:

futreInvestmentValue = investmentAmount * ((1 + monthlyInterestRate)
** numberOfMonths)

以下是輸出樣本:
```
Enter investment amount:1000
Enter annual interest rate:4.25
Enter number of years:1
Accumulated value is 1043.33
```
"""


investmentAmount = eval(input("Enter investment amount:"))
yearsInterestRate = eval(input("Enter annual interest rate:"))
numberOfYears = eval(input("Enter number of years:"))

numberOfMonths = numberOfYears * 12
monthlyInterestRate = yearsInterestRate / 1200
futreInvestmentValue = investmentAmount * ((1 + monthlyInterestRate)
                                           ** numberOfMonths)

print("Accumulated value is", futreInvestmentValue)
