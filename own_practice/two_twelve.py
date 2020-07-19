"""
程式設計練習題 2.2-2.10 2.12 列印表格.

請撰寫一程式，顯示以下這個表格:
```
a     b     a ** b
1     2     1
2     3     8
3     4     81
4     5     1024
5     6     15625
```
"""

A_PRINT = 1
B_PRINT = 2
AB = A_PRINT ** B_PRINT

print("a", "b", "a ** b")
print(A_PRINT, B_PRINT, AB)

A_PRINT += 1
B_PRINT += 1
AB = A_PRINT ** B_PRINT
print(A_PRINT, B_PRINT, AB)

A_PRINT += 1
B_PRINT += 1
AB = A_PRINT ** B_PRINT
print(A_PRINT, B_PRINT, AB)

A_PRINT += 1
B_PRINT += 1
AB = A_PRINT ** B_PRINT
print(A_PRINT, B_PRINT, AB)

A_PRINT += 1
B_PRINT += 1
AB = A_PRINT ** B_PRINT
print(A_PRINT, B_PRINT, AB)

A_PRINT += 1
B_PRINT += 1
AB = A_PRINT ** B_PRINT
print(A_PRINT, B_PRINT, AB)
