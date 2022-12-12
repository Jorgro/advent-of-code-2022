

monkeys = {}
import numpy as np

from math import sqrt
def factors(n):
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                yield i
                break
def moduloMultiplication(a, b, mod):

    res = 0; # Initialize result

    # Update a if it is more than
    # or equal to mod
    a = a % mod;

    while (b):

        # If b is odd, add a with result
        if (b & 1):
            res = (res + a) % mod;

        # Here we assume that doing 2*a
        # doesn't cause overflow
        a = (2 * a) % mod;

        b >>= 1; # b = b / 2

    return res;

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

            #if self.operation[0] == "*" and self.operation[1] == "old":
                #new_facs = []
                #for fac in item[0]:
                #    new_facs.append(fac)
                #for fac in new_facs:
                #    item[0].append(fac)

            # elif self.operation[0] == "*":
            #     val = int(self.operation[1])
            #     for fac in factors(val):
            #         #if fac not in item[0]:
            #         item[0].append(fac)
            # else:

            #     val = int(self.operation[1])
            #     item[1].append(val)
                # ((A % C) + (B % C)) % C


            sum_mod = 1
            for i in item[0]:
                sum_mod *= i % self.divisor
            for i in item[1]:
                sum_mod += i % self.divisor

            if sum_mod % self.divisor == 0:
                    monkeys[self.true_monk].addItem(item)
            else:
                monkeys[self.false_monk].addItem(item)

            # if self.operation[1] == "old":
            #     val = item
            # else:
            #     val = int(self.operation[1])

            # if self.operation[0] == "*":
            #     item *= val
            # else:
            #     item += val

            # #item /= 3
            # #item = int(item)

            # if not moduloMultiplication():
            #     monkeys[self.true_monk].addItem(item)
            # else:
            #     monkeys[self.false_monk].addItem(item)

        self.items = []

    def __str__(self) -> str:
        return str(self.items)


class Item:

    def __init__(self, val, owner):
        self.monkeys = {}
        self.val = val
        self.owner = owner


with open("day11/input.txt", "r") as f:

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

items = []
for key, monkey in monkeys.items():
    for item in monkey.items:
        items.append(Item(item, key))

for item in items:
    for key, monkey in monkeys.items():
        item.monkeys[key] = [item.val % monkey.divisor, monkey.divisor]

for _ in range(10000):
    for key, monkey in monkeys.items():
        for item in items:
            if item.owner == key:
                monkey.inspections += 1
                for key2, monk in item.monkeys.items():
                    if monkey.operation[0] == "*" and monkey.operation[1] == "old":
                        item.monkeys[key2][0] *= item.monkeys[key2][0]
                    elif monkey.operation[0] == "*":
                        val = int(monkey.operation[1]) % monk[1]
                        item.monkeys[key2][0] *= val
                    else:
                        val = int(monkey.operation[1]) % monk[1]
                        item.monkeys[key2][0] += val
                    item.monkeys[key2][0] = item.monkeys[key2][0] % monk[1]

                if not item.monkeys[key][0]:
                    item.owner = monkey.true_monk
                else:
                    item.owner = monkey.false_monk

print(items[0].monkeys)

# for j in range(1000):

#     if not j % 100:
#         print(j)

#     for key, monkey in monkeys.items():
#         monkey.doRound()

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
