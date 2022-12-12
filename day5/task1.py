stacks = [
    ['F', 'D', 'B', 'Z', 'T', 'J', 'R', 'N'],
    ['R', 'S', 'N', 'J', 'H'],
    ['C', 'R', 'N', 'J', 'G', 'Z', 'F', 'Q'],
    ['F', 'V', 'N', 'G', 'R', 'T', 'Q'],
    ['L', 'T', 'Q', 'F'],
    ['Q', 'C', 'W', 'Z', 'B', 'R', 'G', 'N'],
    ['F', 'C', 'L', 'S', 'N', 'H', 'M'],
    ['D', 'N', 'Q', 'M', 'T', 'J'],
    ['P', 'G', 'S']
]

with open("day5/input.txt", "r") as f:
    for line in f:
        line = line.strip().split(" ")

        nr = int(line[1])
        ind_fr = int(line[3])-1
        ind_to = int(line[5])-1

        els = []
        for _ in range(nr):
            el = stacks[ind_fr].pop()
            els.insert(0, el)

        #print(els)
        for el in els:
            stacks[ind_to].append(el)
        #stacks[ind_to].append(stacks[ind_fr][len(stacks[ind_fr])-nr-1:])
        #del stacks[ind_fr][len(stacks[ind_fr])-nr-1:]

for j in stacks:
    print(j[-1])
