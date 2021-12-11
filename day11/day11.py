with open('input.txt') as f:
    matrix = [[int(i) for i in line.strip()] for line in f.readlines()]

rowsncols = [(r, c) for r in range(len(matrix)) for c in range(len(matrix[r]))]

def get_adjacent(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]

total_flashes = 0
for step in range(100):
    flashing = []

    for r,c in rowsncols:
        matrix[r][c]+=1
        if matrix[r][c]>9:
            flashing.append((r,c))

    while flashing:
        curflash = flashing.pop()
        if matrix[curflash[0]][curflash[1]]==0:
            continue

        total_flashes+=1
        matrix[curflash[0]][curflash[1]]=0
        for n in get_adjacent(*curflash):
            if n in rowsncols and matrix[n[0]][n[1]] !=0:
                matrix[n[0]][n[1]] += 1
                if matrix[n[0]][n[1]] > 9:
                    flashing.append(n)

print(total_flashes)

# Part 2 - reset matrix lol
with open('input.txt') as f:
    matrix = [[int(i) for i in line.strip()] for line in f.readlines()]

step = 0
while True:
    step += 1
    flashing = []
    for r,c in rowsncols:
        matrix[r][c]+=1
        if matrix[r][c]>9:
            flashing.append((r,c))

    while flashing:
        curflash = flashing.pop()
        if matrix[curflash[0]][curflash[1]]==0:
            continue

        matrix[curflash[0]][curflash[1]]=0

        for n in get_adjacent(*curflash):
            if n in rowsncols and matrix[n[0]][n[1]] !=0:
                matrix[n[0]][n[1]] += 1
                if matrix[n[0]][n[1]] > 9:
                    flashing.append(n)

    if all(matrix[r][c]==0 for r,c in rowsncols):
        break

print(step)