

import numpy as np


# ......
# ......
# HT....
# ......
# s.....


#start_ind = (100, 100)

visited = np.zeros((1000, 1000))


def stillTouching(head, tail):
    return (abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1)

print(stillTouching((10, 12), (0, 0)))
#print(stillTouching((2, 2), (2, 0)))

head = [100, 100]
tail = [100, 100]

visited[tail[0], tail[1]] = 1

with open("day9/input.txt","r") as f:

    for line in f:
        line = line.rstrip().split(" ")
        command = line[0]
        steps = int(line[1])


        for step in range(steps):
            prev_pos = head.copy()
            if command == "R":
                head[1] += 1
            elif command == "L":
                head[1] -= 1
            elif command == "U":
                head[0] -= 1
            elif command == "D":
                head[0] += 1
            if not stillTouching(head, tail):
                tail = prev_pos
                visited[tail[0], tail[1]] = 1

print(np.sum(visited))
