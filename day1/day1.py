


with open("day1/input.txt", "r") as f:
    cals = []
    number = 0
    for line in f:
        if line == "\n":
            cals.append(number)
            number = 0
        else:
            number += int(line.strip("\n"))

    print(sum(sorted(cals, reverse=True)[:3]))
