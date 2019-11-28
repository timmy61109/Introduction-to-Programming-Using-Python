"""
程式設計練習題 2.2-2.10 3.8 財務應用:貨幣單位.

請解決範例程式3.4 ComputeChange.py的float轉成int導致的精確度遺失，以輸入「分」(cents)方式
解決。
"""
# Receive the amount
amount = eval(input("Enter an amount in cents, e.g., 1156: "))

# Convert the amount to cents
remainingAmount = int(amount)

# Find the number of one dollars
numberOfOneDollars = int(remainingAmount / 100)
remainingAmount = int(remainingAmount % 100)

# Find the number of quarters in the remaining amount
numberOfQuarters = int(remainingAmount / 25)
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = int(remainingAmount / 10)
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = int(remainingAmount / 5)
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display results
print("Your amount", amount, "consists of\n",
      "\t", numberOfOneDollars, "dollars\n",
      "\t", numberOfQuarters, "quarters\n",
      "\t", numberOfDimes,  "dimes\n",
      "\t", numberOfNickels, "nickels\n",
      "\t", numberOfPennies, "pennies")
