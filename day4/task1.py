
import re


total = 0
with open("day4/input.txt", "r") as f:
    for line in f:
        s = re.split(",|-", line.strip())

        elf1 = (int(s[0]), int(s[1]))
        elf2 = (int(s[2]), int(s[3]))
        print("1:", elf1)
        print("2:", elf2)

        if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
            total += 1
        elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
            total += 1
print(total)
