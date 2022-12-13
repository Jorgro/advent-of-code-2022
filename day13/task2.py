import json


data = []

with open("day13/input.txt", "r") as f:

    #curr_comp = []

    for line in f:
        line = line.strip()
        if line:
            data.append(json.loads(line))


def compare(left, right):
    #print("Comparing: ")
    #print(left)
    #print(right)

    if not isinstance(left, list) and not isinstance(right, list):
        if left == right:
            return 0
        else:
            if left < right:
                return 1
            else:
                return -1
    elif isinstance(left, list) and isinstance(right, list):

        cmp = 0
        i = 0
        while i < len(left) and cmp == 0:
            if i == len(right):
                return -1 # Right side ran out of items
            else:
                cmp = compare(left[i], right[i])
            i += 1

        if cmp == 0:
            if i == len(left) and i == len(right):
                return 0 # Same amount of items and no conclusion reached
            else:
                return 1 #
        return cmp

        # if i == len(left) and cmp == "c": #and i < len(right):
        #     cmp = True

        # return cmp
    else:
        if not isinstance(left, list):
            left = [left]
        else:
            right = [right]
        return compare(left, right)

from functools import cmp_to_key
#sorted_data = sorted(data, key=compare)
data.sort(key=cmp_to_key(compare), reverse=True)
print(data)

print((data.index([[2]])+1)*(data.index([[6]])+1))
