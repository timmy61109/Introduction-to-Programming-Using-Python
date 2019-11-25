"""
程式設計練習題 3.3-3.6 3.11 反轉數字.

請撰寫一程式，提示使用者輸入四位數的整數，然後以反轉的順序加以印出，以下是程式輸出的樣本:

```

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
