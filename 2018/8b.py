class Node:
    def __init__(self):
        self.children = []
        self.metadata = []


with open("8.txt") as f:
    t = f.read()
t.rstrip()
t = tuple(map(int, t.split()))
# print(t)

stack_num_node = [1]
stack_num_meta = [0]

suma = 0
i = 0

root = Node()
stack_node = [root]

while i < len(t):
    num_nodes = t[i]
    num_meta = t[i + 1]
    n = Node()
    stack_node[-1].children.append(n)
    if num_nodes == 0:
        n.metadata.extend(t[i + 2 : i + 2 + num_meta])
        suma += sum(t[i + 2 : i + 2 + num_meta])
        i = i + 2 + num_meta
        stack_num_node[-1] -= 1
        while stack_num_node[-1] == 0:
            stack_num_node.pop()
            stack_node[-1].metadata.extend(t[i : i + stack_num_meta[-1]])
            suma += sum(t[i : i + stack_num_meta[-1]])
            i = i + stack_num_meta[-1]
            stack_num_meta.pop()
            stack_node.pop()
            if not stack_num_node:
                break
            stack_num_node[-1] -= 1
    else:
        stack_num_node.append(num_nodes)
        stack_num_meta.append(num_meta)
        stack_node.append(n)
        i = i + 2


def value(node):
    if not node.children:
        return sum(node.metadata)
    ret = 0
    for m in node.metadata:
        if m - 1 < len(node.children):
            ret += value(node.children[m - 1])
    return ret


root = root.children[0]
print(value(root))

print(suma)


# One Little Victory !!!
