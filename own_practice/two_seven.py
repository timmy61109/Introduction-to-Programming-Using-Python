"""
程式設計練習題 2.2-2.10 2.7 找出年數.

請撰寫一程式，提示使用者輸入分鐘數(例如十億)，接著顯示相對應的年數與天數。假設一年365天。以下是
範例輸出樣本:
```
Enter a number of minutes:1000000000
1000000000 minutes is approximately 1902 years and 1000000000 days
```
"""
import ast


minutes = ast.literal_eval(input("Enter a number of minutes:"))
days = minutes // 1440
years = days // 365

print(minutes, "minutes is approximately", years, "years and", days, "days")
