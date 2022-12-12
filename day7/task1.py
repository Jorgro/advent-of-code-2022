

class Node:
    def __init__(self, name, parent=None, value=None):
        self.parent = parent
        self.value = value
        self.name = name
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def getSize(self):
        #print(self.children)
        if not self.children:
            return self.value

        tot = 0
        for child in self.children:
            #print(child)
            tot += child.getSize()

        return tot

    def __str__(self):
        return f"Node {self.name}: {self.value}"

nodes = {}
with open("day7/input.txt", "r") as f:
    lines = [line.rstrip().split(" ") for line in f]

    current_node = Node("/")
    nodes[current_node.name] = current_node
    i = 1
    while i < len(lines):
        line = lines[i]

        if line[0] == "$":
            if line[1] == "cd":
                if line[2] != "..":
                    #if current_node.name + "/" + line[2] not in nodes.keys():
                    #    current_node = Node(current_node.name + "/" + line[2], current_node)
                    #    nodes[current_node.name + "/" + line[2]] = current_node
                    #else:
                    current_node = nodes[current_node.name + "/" + line[2]]
                else: # cd ..
                    current_node = current_node.parent
        elif line[0] == "dir":
            new_child = Node(current_node.name + "/" + line[1], current_node)
            current_node.addChild(new_child)
            nodes[new_child.name] = new_child
        else:
            size = int(line[0])
            name = current_node.name + "/" + line[1]
            new_child = Node(name, current_node, size)
            current_node.addChild(new_child)
            nodes[new_child.name] = new_child
        i += 1

#for child in nodes["//a/a"].children:
#    print(child.getSize())
#print((nodes["//a/a"].children)
# tot = 0
# for key, node in nodes.items():
# #    print(key)
#     if node.value == None:
#         size = node.getSize()
#         if size <= 100000:
#             tot += node.getSize()
#     #print(f"Node {node}: {node.getSize()}")
# print(tot)
free_space = 70000000- nodes["/"].getSize()
needed_space = 30000000 - free_space
print(needed_space)


least_space = 70000000
least_space_node = None
for key, node in nodes.items():

    if node.value == None:
        size = node.getSize()
        if size >= needed_space and size < least_space:
            least_space = size
            least_space_node = node
print(least_space)
    #print(f"Node {node}: {node.getSize()}")
                    # i += 1
                    # new_l = lines[i]
                    # while new_l[0] == "$":
                    #     i += 1
                    #     new_l = lines[i]
