import re

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

distances = {}

min_x = 10000000000
min_y = 10000000000
max_y = 0
max_x = 0

min_x_s = None
max_x_s = None
beacons = []
coords = []
with open("day15/input.txt", "r") as f:

    for line in f:
        numbers = re.compile('-?\d+')
        res = list(map(int, numbers.findall(line)))
        #res[0] += 2
        #res[2] += 2

        # if res[0] > max_x:
        #     max_x = res[0]
        #     max_x_s = (res[1], res[0])

        # if res[0] < min_x:
        #     min_x = res[0]
        #     min_x_s = (res[1], res[0])

        # #if res[2] > max_x:
        # #    max_x = res[2]

        # #if res[2] < min_x:
        # #    min_x = res[2]

        # if res[1] > max_y:
        #     max_y = res[1]

        # if res[1] < min_y:
        #     min_y = res[1]


        #if res[3] > max_y:
        #    max_y = res[3]

        #if res[3] < min_y:
        #    min_y = res[3]

        distances[(res[1], res[0])] = manhattan((res[1], res[0]), (res[3], res[2]))

        if res[0] + distances[(res[1], res[0])] > max_x:
            max_x = res[0] + distances[(res[1], res[0])]
            max_x_s = (res[1], res[0])

        if res[0] - distances[(res[1], res[0])] < min_x:
            min_x = res[0] - distances[(res[1], res[0])]
            min_x_s = (res[1], res[0])

        #coords.append([res[1], res[0], res[3], res[2]])
        #beacons.append((res[3], res[2]))

#print(max_y - min_y)
#print(max_x- min_x)
#arr = [["." for column in range(max_x-min_x)]
#                      for row in range(max_y-min_y)]

# for c in coords:
#     #c[0] -= min_y
#     #c[2] -= min_y
#     #c[1] -= min_x
#     #c[3] -= min_x
#     #arr[c[0]][c[1]] = "S"
#     #arr[c[2]][c[3]] = "B"

#     #arr[c[0]][c[1]] = "S"
#     #arr[c[2]][c[3]] = "B"

#     distances[(c[0], c[1])] = manhattan((c[0], c[1]), (c[2], c[3]))
#print(min_x - distances[min_x_s])
print(min_x)

import numpy as np
arr = np.zeros(max_x + distances[max_x_s] + distances[min_x_s]+20)
for key, val in distances.items():
    dist = manhattan(key, [2000000, key[1]])
    if dist <= val:
        print(key)
        print(val)
        print(dist)
        #print(val-dist)
        print("start: ", key[1]-(val-dist)-min_x)
        print("end: ", key[1]+(val-dist)+1-min_x)

        arr[key[1]-(val-dist)-min_x:key[1]+(val-dist)+1-min_x] = 1
s = np.sum(arr)
print(int(s)-1)


    #if manhattan((2000000, i), key) <= val:


# for i in range(min_x - distances[min_x_s], max_x - distances[max_x_s]):
#     for key, val in distances.items():
#         if manhattan((2000000, i), key) <= val:
#             count += 1

# for key, val in distances.items():
#     for i in range(len(arr)):
#         for j in range(len(arr[1])):
#             if manhattan(key, [i, j]) <= val:
#                 if arr[i][j] == ".":
#                     arr[i][j] = "#"
#for row in arr:
#    print()
#    for j in row:
#        print(j, end="")

#print(arr[10].count("#"))
