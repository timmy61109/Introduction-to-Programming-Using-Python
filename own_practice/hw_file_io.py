"""讀入HW1in.txt 輸出HW1out.txt."""

with open('HW1in.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    print(text)

with open('HW1out.txt', 'w', encoding='utf-8') as file:
    for value in text:
        file.write(value)
        if value == "\n":
            file.write('\n')
