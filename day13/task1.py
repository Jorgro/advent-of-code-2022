import json


data = []

with open("day13/input.txt", "r") as f:

    curr_comp = []

    for line in f:
        line = line.strip()

        if line:
            curr_comp.append(json.loads(line))
        else:
            data.append(curr_comp)
            curr_comp = []


def compare(left, right):
    #print("Comparing: ")
    #print(left)
    #print(right)

    if not isinstance(left, list) and not isinstance(right, list):
        if left == right:
            return "c"
        else:
            return left < right
    elif isinstance(left, list) and isinstance(right, list):

        cmp = "c"
        i = 0
        while i < len(left) and cmp == "c":
            if i == len(right):
                return False # Right side ran out of items
            else:
                cmp = compare(left[i], right[i])
            i += 1

        if cmp == "c":
            if i == len(left) and i == len(right):
                return "c" # Same amount of items and no conclusion reached
            else:
                return True #
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

#compare(data[1][0], data[1][1])
s = 0
for i, comp in enumerate(data):
    print()
    print(i+1)
    val = compare(comp[0], comp[1])
    print(val)
    if val:
        s += i + 1

print(s)
