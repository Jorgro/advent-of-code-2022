import re
import numpy as np
import math
def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def euclidean(a, b):
    return math.dist(a, b)

def getDist(a, b):
    return a-b

distances = {}


min_x = 10000000000
min_y = 10000000000
max_y = 0
max_x = 0

min_x_s = None
max_x_s = None
beacons = []
coords = []

sources = []
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

        # s_x = res[0]
        # s_y = res[1]

        # side = manhattan((res[1], res[0]), (res[3], res[2]))

        # start_x = s_x - side
        # start_y = s_y

        # sources.append((start_y, start_x))


#for


        distances[(res[1], res[0])] = manhattan((res[1], res[0]), (res[3], res[2]))

        # if res[0] + distances[(res[1], res[0])][0] > max_x:
        #     max_x = res[0] + distances[(res[1], res[0])][0]
        #     max_x_s = (res[1], res[0])

        # if res[0] - distances[(res[1], res[0])][0] < min_x:
        #     min_x = res[0] - distances[(res[1], res[0])][0]
        #     min_x_s = (res[1], res[0])

        # if res[1] + distances[(res[1], res[0])][0] > max_y:
        #     max_y = res[1] + distances[(res[1], res[0])][0]
        #     max_y_s = (res[1], res[0])

        # if res[1] - distances[(res[1], res[0])][0] < min_y:
        #     min_y = res[1] - distances[(res[1], res[0])][0]
        #     min_y_s = (res[1], res[0])

        #coords.append([res[1], res[0], res[3], res[2]])
        # if (res[3], res[2]) not in beacons:
        #     beacons.append((res[3], res[2]))

#print(min_x)
#print(max_x)
#print(min_y)
#print(max_y)
#distances[(0, 0)] = [1]
#distances[(0, 4000000)] = [1]
#distances[(4000000, 0)] = [1]
#distances[(4000000, 4000000)] = [1]

# potentials = []
# for key1, val1 in distances.items():
#     for key2, val2 in distances.items():
#         if key2 != key1:
#             mid_x_f = math.floor((key1[1]+key2[1]) / 2)
#             mid_x_c = math.ceil((key1[1]+key2[1]) / 2)
#             mid_y_f = math.floor((key1[0]+key2[0]) / 2)
#             mid_y_c = math.ceil((key1[0]+key2[0]) / 2)

#             for x in [mid_x_f, mid_x_c]:
#                 for y in [mid_y_f, mid_y_c]:
#                     if manhattan([y, x], key1) > val1 and manhattan([y, x], key2) > val2:
#                         if [y, x] not in potentials:
#                             potentials.append([y, x])



# print(potentials)

k = 4000001
#k = 20

def run():
    for i in range(k):
        #print("i:", i)
        j = 0
        while j < k:
            t = True
            for key, val in distances.items():
                dist = manhattan(key, [i, j])
                if manhattan(key, [i, j]) <= val:
                    j = key[1] + val + 1 - abs(key[0]-i)
                    #j = (val-dist) + 1 - ((key[1]-i))
                    t = False
                    break
            if t:
                return i, j
            #print(j)
            #print(i)

        if not i % 100000:
            print(i)

print(3141837*4000000+3400528)
#print(run())
# for p in potentials:
#     t = True
#     for key, val in distances.items():
#         if manhattan(p, key) <= val[0]:
#             t = False
#             break

#     if t:
#         print(p)


# for i in range(100000):
#     arr = np.zeros(4000000)
#     for key, val in distances.items():
#         val = val[0]
#         dist = manhattan(key, [2000000, key[1]])
#         if dist <= val:
#             #print(key)
#             #print(val)
#             #print(dist)
#             #print(val-dist)
#             #print("start: ", key[1]-(val-dist)-min_x)
#             #print("end: ", key[1]+(val-dist)+1-min_x)
#             if key[1]-(val-dist) < 4000000:
#                 if key[1]+(val-dist)+1 > 0:
#                     if key[1]-(val-dist) < 0:
#                         start = 0
#                     else:
#                         start = key[1]-(val-dist)

#                     if key[1]+(val-dist) > 4000000:
#                         end = 4000000
#                     else:
#                         end = key[1]+(val-dist)+1


#                     arr[start:end] = 1

#     s = np.sum(arr)
#     #print(s)
#     if s != 4000000:
#         print(i)

            #print(f"({mid_y}, {mid_x})")

    #print(key)
    #dist = val[0]

    # if key[0] <= 20 and key[0] >= 0 and key[1] <= 20 and key[1] >= 0:
    #     print("Source: ", key)
    #     print(val[1])
    #     s += val[1]
        #print(val[1])

# print(s)
    #print(euclidean([11, 14], key))

# c = 0
# avg_x = 0
# avg_y = 0
# for beacon in beacons:
#     if beacon[0] <= 20 and beacon[0] >= 0 and beacon[1] <= 20 and beacon[1] >= 0:
#         avg_y += beacon[0]
#         avg_x += beacon[1]
#         c += 1
#         print(beacon)

# print("x: ", (avg_x+25)/c)
# print("y: ", (avg_y+17)/c)


# for j in range(4000000):
#     c += 1
# for i in range(4000000):
#     c+= 1
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
# print(min_x)

# import numpy as np

# for j in range(4000000+1):
#     arr = np.zeros(max_x + distances[max_x_s] + distances[min_x_s]+20)
#     for key, val in distances.items():
#         dist = manhattan(key, [j, key[1]])
#         if dist <= val:
#             #print(key)
#             #print(val)
#             #print(dist)
#             #print(val-dist)
#             #print("start: ", key[1]-(val-dist)-min_x)
#             #print("end: ", key[1]+(val-dist)+1-min_x)

#             arr[key[1]-(val-dist)-min_x:key[1]+(val-dist)+1-min_x] = 1
#     s = np.sum(arr)
#     if not j % 1000:
#         print(j)
# print(int(s)-1)




# arr = np.zeros((4000000, 4000000), dtype=bool)

# x_ranges = []
# y_ranges = []
# for key, val in distances.items():
#     dist_x_1 = manhattan(key, [4000000, key[1]])
#     dist_x_2 = manhattan(key, [0, key[1]])
#     dist_y_1 = manhattan(key, [key[0], 4000000])
#     dist_y_2 = manhattan(key, [key[0], 0])

#     if dist_x_1 <= val:
#         print(val-dist_x_1)
#         for i in range(val-dist_x_1):

#         x_ranges.append()
#             arr[i][key[1]-(val-dist_x_1),key[1]+(val-dist_x_1)+1] = True

#     if dist_x_1 <= val:
#         for i in range(val-dist_x_1):
#             arr[i][key[1]-(val-dist_x_1):key[1]+(val-dist_x_1)+1] = True
#     if dist_x_2 <= val:
#         for i in range(val-dist_x_1):
#             arr[i][key[1]-(val-dist_x_1):key[1]+(val-dist_x_1)+1] = True

#     if dist_y_1 <= val:
#         for i in range(val-dist_y_1):
#             #print(i)
#             #print(arr.shape)
#             #print(key[0]-(val-dist_y_1))
#             start = 0
#             if key[0]-(val-dist_y_1) > 0:
#                 start = key[0]-(val-dist_y_1)
#             end = 4000000
#             if key[0]+(val-dist_y_1)+1 < 4000000:
#                 end = key[0]+(val-dist_y_1)+1
#             arr[start:end][i] = True
#     if dist_y_2 <= val:
#         for i in range(val-dist_y_2):
#             arr[key[0]-(val-dist_y_2):key[0]+(val-dist_y_2)+1][i] = True
#         print(key)

#     if manhattan((2000000, i), key) <= val:


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
