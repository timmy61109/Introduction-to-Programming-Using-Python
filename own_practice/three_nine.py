"""
程式設計練習題 3.3-3.6 3.9 財務應用:薪資.

請撰寫一程式，讀取下列資訊並列出與有關資料:

Employee's name (e.g., Smith)
Number of hours worked in a week (e.g., 10)
Hourly pay rate (e.g., 9.75)
Federal tax withholding rate (e.g., 20%)
State tax withholding rate (e.g., 9%)

以下是程式的輸出樣本:
```
Enter employee's name: Smith
Enter number of hours worked in a week: 10
Enter hourly pay rate: 9.75
Enter federal tax wighholding rate: 0.20
Enter state tax withholding rate: 0.09

Employee Name: Smith
Hours Worked: 10.0
Pay Rate: $9.75
Gross Pay: $97.5
Deuctions
    Federal Withholding (20.0%): $19.5
    State Withholding (9.0%): $8.77
    Total Deduction: $28.27
Net Pay: $69.22
```
"""
# Receive the amount
import ast


NAME = str(input("Enter employee's name:"))
HOURS = ast.literal_eval(input("Enter number of hours worked in a week:"))
HOURLY = ast.literal_eval(input("Enter hourly pay rate:"))
FEDERAL = ast.literal_eval(input("Enter federal tax wighholding rate:"))
STATE = ast.literal_eval(input("Enter state tax withholding rate:"))

GROSS_PAY = HOURS * HOURLY
FEDERAL_WITHHOLDING = GROSS_PAY * 0.2
STATE_WITHHOLDING = GROSS_PAY * 0.09
TOTAL_DEDUCTION = FEDERAL_WITHHOLDING + STATE_WITHHOLDING
NET_PAY = GROSS_PAY - TOTAL_DEDUCTION

print("\nEmployee Name:", NAME, "\n",
      "Hours Worked:", HOURS, "\n",
      "Pay Rate $:", HOURLY, "\n",
      "Gross Pay: $", GROSS_PAY, "\n",
      "Deuctions", GROSS_PAY, "\n",
      "  Federal Withholding (20.0%): $", FEDERAL_WITHHOLDING, "\n",
      "  State Withholding (9.0%): $", STATE_WITHHOLDING, "\n",
      "  Total Deduction: $", TOTAL_DEDUCTION, "\n",
      "Net Pay: $", NET_PAY)
