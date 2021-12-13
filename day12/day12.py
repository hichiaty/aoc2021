from collections import defaultdict

with open('input.txt') as f:
    lines = f.readlines()

edge_map = defaultdict(set)
for edge in lines:
    src, dst = edge.strip().split('-')
    edge_map[src].add(dst)
    edge_map[dst].add(src)

completepaths = set()

stack = [('start',)]
while stack:
    path = stack.pop()
    if path[-1] == 'end':
        completepaths.add(path)
        continue

    for choice in edge_map[path[-1]]:
        if choice.isupper() or choice not in path:
            stack.append((*path, choice))

print(len(completepaths))

# part 2 - can reuse graph
stack = [(('start',), False)]
completepaths = set()
while stack:
    path, double_small = stack.pop()
    if path[-1] == 'end':
        completepaths.add(path)
        continue

    for choice in edge_map[path[-1]] - {'start'}:
        if choice.isupper():
            stack.append(((*path, choice), double_small))
        elif double_small is False and path.count(choice) == 1:
            stack.append(((*path, choice), True))
        elif choice not in path:
            stack.append(((*path, choice), double_small))

print(len(completepaths))