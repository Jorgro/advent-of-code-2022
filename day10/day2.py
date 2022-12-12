

with open("day10/input.txt", "r") as f:

    executions = []

    lines = f.readlines()
    j = 0

    for i in range(len(lines)):
        line = lines[i].rstrip().split(" ")
        if line[0] == "addx":
            j += 2
            executions.append((j, int(line[1])))
        else:
            j += 1
            executions.append((j, 0))

print(executions)


to_print = []
sprite = 1
curr_pix = 0
for i in range(1, 241):
    if abs(sprite-curr_pix) <= 1:
        #print("#", end='')
        to_print.append("#")
    else:
        to_print.append(".")
    curr_pix += 1
    if curr_pix == 40:
        curr_pix = 0

    for exec_ in executions:
        if exec_[0] == i:
            sprite += exec_[1]


for i in range(6):
    for j in range(40):
        print(to_print[40*i + j], end="")
    print("\n")
        #print(".", end="")
                # curr_pix += 1

    # X = 1
    # i = 0
    # clock = 0
    # lines = f.readlines()

    # for inter in intervals:
    #     curr_pix = 0
    #     while clock < inter:
    #         if i >= 1:
    #             prev_line = lines[i-1].rstrip().split()
    #             if prev_line[0] == "addx":
    #                 X += int(prev_line[1])

    #         line = lines[i].rstrip().split()
    #         if line[0] == "addx":
    #             clock += 2
    #             # for _ in range(2):
    #             #     if abs(X-curr_pix) <= 1:
    #             #         print("#", end="")
    #             #     else:
    #             #         print(".", end="")
    #             #     curr_pix += 1
    #         else:
    #             clock += 1
    #             if abs(X-curr_pix) <= 1:
    #                  print("#", end='')
    #              else:
    #                  print(".", end="")
    #             # curr_pix += 1

    #         i += 1
    #     print("\n")
        #log.append(X)

        #print(f"{i}: {X}")
##......................................
