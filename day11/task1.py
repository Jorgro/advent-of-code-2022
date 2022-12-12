

monkeys = {}

class Monkey:

    def __init__(self) -> None:
        self.items = []
        self.true_monk = None
        self.false_monk = None
        self.inspections = 0

    def setDivisor(self, divisor):
        self.divisor = divisor


    def addItem(self, item):
        self.items.append(item)

    def setOperation(self, operation):
        self.operation = operation


    def doRound(self):

        for item in self.items:
            self.inspections += 1

            if self.operation[1] == "old":
                val = item
            else:
                val = int(self.operation[1])

            if self.operation[0] == "*":
                item *= val
            else:
                item += val

            item /= 3
            item = int(item)

            if not item % self.divisor:
                monkeys[self.true_monk].addItem(item)
            else:
                monkeys[self.false_monk].addItem(item)
        self.items = []

    def __str__(self) -> str:
        return str(self.items)

with open("day11/test.txt", "r") as f:

    for line in f:
        line = line.strip().replace(",", "").split(" ")

        if line[0] == "Monkey":
            curr_monkey = Monkey()
            monkeys[line[1][0]] = curr_monkey
        elif line[0] == "Starting":

            for j in range(2, len(line)):
                curr_monkey.addItem(int(line[j]))

        elif line[0] == "Operation:":
            op = line[4]
            val = line[5]
            curr_monkey.setOperation((op, val))

        elif line[0] == "Test:":
            curr_monkey.setDivisor(int(line[3]))

        elif line[0] == "If" and line[1] == "true:":
            curr_monkey.true_monk = line[5]
        elif line[0] == "If" and line[1] == "false:":
            curr_monkey.false_monk = line[5]

for j in range(10000):

    if not j % 100:
        print(j)

    for key, monkey in monkeys.items():
        monkey.doRound()

    #print("Round: ", j)
    # for key, monkey in monkeys.items():
    #     print(f"Monkey {key}: {monkey}")

print()

inspections = []
for key, monkey in monkeys.items():
    print(f"Monkey {key}: {monkey.inspections}")
    inspections.append(monkey.inspections)


import numpy as np

ind = np.argpartition(inspections, -2)[-2:]

print(inspections[ind[0]]*inspections[ind[1]])
