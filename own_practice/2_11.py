"""
程式設計練習題 2.2-2.10 2.11 財務金融應用程式:投資理財總額.

假設您以固定的年率利儲存一筆金額於活期存款帳戶。需要存多少前才能在三年後帳戶會有$5000?
可利用下
列公式獲得最初的存款金額:

initialDepositAmount = finalAccountValue / (1 + monthlyInterestRate) ** \
numberOfMonths

撰寫一程式，提示使用者輸入帳戶總額、年利率，以及年數，然後顯示最初的存款金額。以下是範例輸出樣本:

```
Enter final account value: 1000
Enter annual interrest rate in percent: 4.25
Enter number of years: 5
Initial deposit value is 808.8639197424636
```
"""

finalAccountValue = eval(input("Enter final account value:"))
AnnualInterestRate = eval(input("Enter annual interrest rate in percent:"))
numberOfYears = eval(input("Enter number of years:"))

numberOfMonths = numberOfYears * 12
monthlyInterestRate = AnnualInterestRate / 1200

initialDepositAmount = finalAccountValue / (1 + monthlyInterestRate) ** \
                                            numberOfMonths

print("Initial deposit value is", initialDepositAmount)
