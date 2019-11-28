"""
程式設計練習題 2.2-2.10 3.6 尋找ASCII碼所對應的字元.

請撰寫一程式，輸入一個介於0~127之間整數的ASCII碼輸出對應字元，以下是程式的執行結果:
```
Enter an ASCII code:69
The character is E
```
"""
number = eval(input("Enter an ASCII code:"))

character = chr(number)

print("The character is", character)
