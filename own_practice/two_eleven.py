r"""
程式設計練習題 2.2-2.10 2.11 財務金融應用程式:投資理財總額.

假設您以固定的年率利儲存一筆金額於活期存款帳戶。需要存多少前才能在三年後帳戶會有$5000?
可利用下
列公式獲得最初的存款金額:

initialDepositAmount = FINAL_ACCOUNT_VALUE / (1 + monthlyInterestRate) ** \
numberOfMonths

撰寫一程式，提示使用者輸入帳戶總額、年利率，以及年數，然後顯示最初的存款金額。以下是範例輸出樣本:

```
Enter final account value: 1000
Enter annual interrest rate in percent: 4.25
Enter number of years: 5
Initial deposit value is 808.8639197424636
```
"""

FINAL_ACCOUNT_VALUE = int(input("Enter final account value:"))
ANNUAL_INTEREST_RATE = int(input("Enter annual interrest rate in percent:"))
NUMBER_OF_YEARS = int(input("Enter number of years:"))

NUMBER_OF_MONTHS = NUMBER_OF_YEARS * 12
MONTHLY_INTEREST_RATE = ANNUAL_INTEREST_RATE / 1200

INITIAL_DEPOSIT_AMOUNT = FINAL_ACCOUNT_VALUE / (1 + MONTHLY_INTEREST_RATE) ** \
                                            NUMBER_OF_MONTHS

print("Initial deposit value is", INITIAL_DEPOSIT_AMOUNT)
