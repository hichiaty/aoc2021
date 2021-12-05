from collections import defaultdict

with open('input.txt', 'r') as f:
    data = f.readlines()
    data = [(x1y1, x2y2) for x1y1, x2y2 in [line.strip().split(' -> ') for line in data]]

points_covered = defaultdict(lambda: 0)
for x1y1, x2y2 in data:
    x1 = int(x1y1.split(',')[0])
    y1 = int(x1y1.split(',')[1])
    x2 = int(x2y2.split(',')[0])
    y2 = int(x2y2.split(',')[1])
    # consider only horizontal and vertical lines
    if x1 == x2:
        for y in range(min(y1,y2), max(y1,y2) + 1):
            points_covered[(x1, y)] += 1
    elif y1 == y2:
        for x in range(min(x1,x2), max(x1,x2) + 1):
            points_covered[(x, y1)] += 1

print(len([x for x in points_covered.values() if x >= 2]))

# part 2
points_covered = defaultdict(lambda: 0)
for x1y1, x2y2 in data:
    x1 = int(x1y1.split(',')[0])
    y1 = int(x1y1.split(',')[1])
    x2 = int(x2y2.split(',')[0])
    y2 = int(x2y2.split(',')[1])
    # consider horizontal vertical and diagonal lines
    if x1 == x2:
        for y in range(min(y1,y2), max(y1,y2) + 1):
            points_covered[(x1, y)] += 1
    elif y1 == y2:
        for x in range(min(x1,x2), max(x1,x2) + 1):
            points_covered[(x, y1)] += 1
    else:
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        while x1 != x2 and y1 != y2:
            points_covered[(x1,y1)] += 1
            x1 += x_step
            y1 += y_step
        points_covered[(x1, y1)] += 1

print(len([x for x in points_covered.values() if x >= 2]))
