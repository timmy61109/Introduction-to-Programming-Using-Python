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
name = str(input("Enter employee's name:"))
hours = eval(input("Enter number of hours worked in a week:"))
hourly = eval(input("Enter hourly pay rate:"))
federal = eval(input("Enter federal tax wighholding rate:"))
state = eval(input("Enter state tax withholding rate:"))

gross_pay = hours * hourly
federal_withholding = gross_pay * 0.2
state_withholding = gross_pay * 0.09
total_deduction = federal_withholding + state_withholding
net_pay = gross_pay - total_deduction

print("\nEmployee Name:", name, "\n",
      "Hours Worked:", hours, "\n",
      "Pay Rate $:", hourly, "\n",
      "Gross Pay: $", gross_pay, "\n",
      "Deuctions", gross_pay, "\n",
      "  Federal Withholding (20.0%): $", federal_withholding, "\n",
      "  State Withholding (9.0%): $", state_withholding, "\n",
      "  Total Deduction: $", total_deduction, "\n",
      "Net Pay: $", net_pay)
