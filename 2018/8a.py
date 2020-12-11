class Node:
    def __init__(self):
        children = []
        metadata = []


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
stack_node = []

while i < len(t):
    num_nodes = t[i]
    num_meta = t[i + 1]
    if num_nodes == 0:
        suma += sum(t[i + 2 : i + 2 + num_meta])
        i = i + 2 + num_meta
        stack_num_node[-1] -= 1
        while stack_num_node[-1] == 0:
            stack_num_node.pop()
            suma += sum(t[i : i + stack_num_meta[-1]])
            i = i + stack_num_meta[-1]
            stack_num_meta.pop()
            if not stack_num_node:
                break
            stack_num_node[-1] -= 1
    else:
        stack_num_node.append(num_nodes)
        stack_num_meta.append(num_meta)
        i = i + 2

print(suma)

# Hardest puzzle yet, took me more than two hours.
