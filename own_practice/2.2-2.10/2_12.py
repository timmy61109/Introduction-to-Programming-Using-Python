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

a = 1
b = 2
ab = a ** b

print("a", "b", "a ** b")
print(a, b, ab)

a += 1
b += 1
ab = a ** b
print(a, b, ab)

a += 1
b += 1
ab = a ** b
print(a, b, ab)

a += 1
b += 1
ab = a ** b
print(a, b, ab)

a += 1
b += 1
ab = a ** b
print(a, b, ab)

a += 1
b += 1
ab = a ** b
print(a, b, ab)
