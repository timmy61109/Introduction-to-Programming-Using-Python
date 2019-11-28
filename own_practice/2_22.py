"""
程式設計練習題 2.2-2.10 2.21 人口預測.

使用程式設計練習題 1.11輸入年數，顯示最後的人口。
以下是輸出樣本:
```
Enter the number of years:5
The population in 5 years is 325932970
```
"""

years = eval(input("Enter the number of years:"))

population = 312032486 + years * (((365 * 24 * 3600) / 7)
                                  - ((365 * 24 * 3600) / 13)
                                  + ((365 * 24 * 3600) / 45))

print("The population in ", years, " years is", int(population))
