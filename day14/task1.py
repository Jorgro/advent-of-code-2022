

arr = [["." for column in range(1000)]
                      for row in range(165)]

with open("day14/input.txt", "r") as f:

    highest_row = 0

    for line in f:
        line = line.strip().split("->")

        start = line[0].strip().split(",")
        start = [int(i) for i in start]

        for i in range(1, len(line)):
            nxt = line[i].strip().split(",")
            nxt = [int(x) for x in nxt]

            min_row = min(start[1], nxt[1])
            max_row = max(start[1], nxt[1]) + 1
            min_col = min(start[0], nxt[0])
            max_col = max(start[0], nxt[0]) +1
            if max_row > highest_row:
                highest_row = max_row + 1
            for j in range(min_row, max_row):
                for k in range(min_col, max_col):
                    arr[j][k] = "#"
            start = nxt

for k in range(0, 1000):
    arr[highest_row][k] = "#"

# for row in arr:
#         print("\n")
#         for k in row:
#             print(k, end='')

print(highest_row)

def able_to_move(ind):
    #print(ind)

    if arr[ind[0]+1][ind[1]] == ".":
        new_ind = [ind[0]+1, ind[1]]
        return True, new_ind
    elif arr[ind[0]+1][ind[1]-1] == ".":
        new_ind = [ind[0]+1, ind[1]-1]
        return True, new_ind
    elif arr[ind[0]+1][ind[1]+1] == ".":
        new_ind = [ind[0]+1, ind[1]+1]
        return True, new_ind
    return False, ind

def add_sand():
    start_ind = [0, 500]

    cont, ind = able_to_move(start_ind)
    if ind[0] == 0:
            return False

    while cont:
        cont, ind = able_to_move(ind)
        #print(ind)
        if ind[0] == 0: #and ind[1] == 10:
            return False
    arr[ind[0]][ind[1]] = "o"
    return True


count = 0
first = add_sand()
while first:
    first = add_sand()
    # print()
    # for row in arr:
    #     print("\n")
    #     for k in row:
    #         print(k, end='')

    count += 1
#print(arr[1])
for row in arr:
    print("\n")
    for k in row:
        print(k, end='')

print()
flatten_list = [j for sub in arr for j in sub]
print(flatten_list.count("o"))
#print()
#print(count+1)
    # if count >= 5:
    #     break;
