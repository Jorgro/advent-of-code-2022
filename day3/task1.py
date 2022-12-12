

total = 0
with open("day3/input.txt") as f:

    group = []
    i = 1
    for line in f:
        s = line.strip()
        group.append(s)

        if i % 3 == 0:
            print(group)
            common = set(group[0]).intersection(set(group[1]))
            common = ''.join(common.intersection(set(group[2])))
            total += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(common)+1
            group = []
        i += 1

        #print(s1)
        #print(s2)
        #print(common)
print(total)
