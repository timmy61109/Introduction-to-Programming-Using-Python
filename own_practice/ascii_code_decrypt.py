"""ASCII code decrypt."""

ENCRYPTION_CODE = [80, 82, 82, 71, 79, 72, 35, 86, 88, 70, 78, 86]

for value in ENCRYPTION_CODE:
    print(chr(value - 3), end='')
print()
