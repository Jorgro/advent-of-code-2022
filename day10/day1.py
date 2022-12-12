

log = [0 for _ in range(221)]



intervals = [20, 60, 100, 140, 180, 220]
log = []
with open("day10/input.txt", "r") as f:

    X = 1
    i = 1
    clock = 1
    lines = f.readlines()
    for inter in intervals:
        while clock < inter:
            prev_line = lines[i-1].rstrip().split()
            if prev_line[0] == "addx":
                X += int(prev_line[1])

            line = lines[i].rstrip().split()
            if line[0] == "addx":
                clock += 2
            else:
                clock += 1
            i += 1
        log.append(X)

        #print(f"{i}: {X}")
print(log)

s = 0
for j in range(len(intervals)):
    s += intervals[j]*log[j]
    print(intervals[j]*log[j])

print(s)
