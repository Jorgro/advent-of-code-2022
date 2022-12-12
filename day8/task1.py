import numpy as np

arr = []
with open("day8/input.txt", "r") as f:
    for line in f:
        line = list(line.rstrip())
        line = [eval(i) for i in line]
        arr.append(line)

arr = np.array(arr)

# i, j = 1, 2
# val = arr[i,j]
# top = np.flip(arr[:i,j]) < val
# bot = arr[i+1:,j] < val
# left = np.flip(arr[i,:j]) < val
# right = arr[i,j+1:] < val

# dirs = [top, left, right, bot]
# print(dirs)
# dir_scores = []
# for dir_ in dirs:
#     if dir_.all():
#         dir_scores.append(len(dir_))
#     else:
#         dir_scores.append(np.argmin(dir_)+1)
# print(dir_scores)
# score = np.prod(dir_scores)
# print(score)

highest = -1

for i in range(1, arr.shape[0]-1):
    for j in range(1, arr.shape[1]-1):
        val = arr[i,j]
        top = np.flip(arr[:i,j]) < val
        bot = arr[i+1:,j] < val
        left = np.flip(arr[i,:j]) < val
        right = arr[i,j+1:] < val

        dirs = [top, left, right, bot]
        dir_scores = []
        for dir_ in dirs:
            if dir_.all():
                dir_scores.append(len(dir_))
            else:
                dir_scores.append(np.argmin(dir_)+1)
        score = np.prod(dir_scores)
        if score > highest:
            highest = score
print(highest)
        #print(score)
        # if (top.all() or bot.all() or right.all() or left.all()):



        #     #print("i: ", i)
        #     #print("j: ", j)
        #     counter += 1
