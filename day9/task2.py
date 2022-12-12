

import numpy as np
import copy
# ......
# ......
# HT....
# ......
# s.....


#start_ind = (100, 100)


visited = np.zeros((1000, 1000))

def stillTouching(head, tail):
    return (abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1)

def getDirection(head, tail):
    if stillTouching(head, tail):
        return (0, 0)


    ver = head[0] - tail[0]
    hor = head[1] - tail[1]

    if ver > 0 and hor > 0:
        return (1, 1)
    elif ver < 0 and hor < 0:
        return (-1, -1)
    elif  ver < 0 and hor > 0:
        return (-1, 1)
    elif  ver > 0 and hor < 0:
        return (1, -1)
    elif ver > 1:
        return (1, 0)
    elif ver < -1:
        return (-1, 0)
    elif hor > 1:
        return (0, 1)
    elif hor < -1:
        return (0, -1)

def printVisited():
    for i in range(visited.shape[0]):
        print("\n")
        for j in range(visited.shape[0]):
            if visited[i, j] == 0:
                print(".", end="")
            else:
                print("#", end="")

heads = [[100, 100], [100, 100], [100, 100], [100, 100], [100, 100], [100, 100], [100, 100], [100, 100], [100, 100], [100, 100]]
tail = [100, 100]
#heads = [[20, 20], [20, 20], [20, 20], [20, 20], [20, 20], [20, 20], [20, 20], [20, 20], [20, 20], [20, 20]]
#tail = [20, 20]

visited[tail[0], tail[1]] = 1

with open("day9/input.txt","r") as f:

    for line in f:
        line = line.rstrip().split(" ")
        command = line[0]
        steps = int(line[1])

        #print("\n")

        for step in range(steps):
            #prev_pos = copy.deepcopy(heads)
            if command == "R":
                heads[0][1] += 1
            elif command == "L":
                heads[0][1] -= 1
            elif command == "U":
                heads[0][0] -= 1
            elif command == "D":
                heads[0][0] += 1


            for i in range(1, len(heads)):
                direction = getDirection(heads[i-1], heads[i])
                #print(direction)
                heads[i][0] += direction[0]
                heads[i][1] += direction[1]
                #if not stillTouching(heads[i-1], heads[i]):
                #    heads[i] = prev_pos[i-1]

                if i == len(heads)-1:
                    visited[heads[-1][0], heads[-1][1]] = 1
            #print(heads)

printVisited()
print(np.sum(visited))
