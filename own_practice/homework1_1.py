"""作業一 Loop, List."""

list1 = [1]

for value in range(1, 11):
    print(list1)
    list1.append(value + list1[value - 1])
