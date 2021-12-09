from collections import deque

with open('input.txt', 'r') as f:
    data = f.readlines()
    matrix = [[int(x) for x in i.strip()] for i in data]
    rows, cols = len(matrix), len(matrix[0])

def is_lowpoint(x,y):
    dirs = [[1,0],[0,1],[-1,0],[0,-1]]
    for dr, dc in dirs:
        new_r, new_c = x+dr, y+dc
        if new_r < 0 or new_c < 0 or new_r >= len(matrix) or new_c >= len(matrix[0]):
            continue
        if matrix[new_r][new_c] <= matrix[x][y]:
            return False
    return True

risk_sum = 0
for r, c in [(r,c) for r in range(len(matrix)) for c in range(len(matrix[0]))]:
    if is_lowpoint(r,c):
        risk_sum += matrix[r][c]+1

print(risk_sum)

#part 2 - bfs boisssssss
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited = set((x,y))
    basin_size = 0
    while q:
        x, y = q.popleft()
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        for dr, dc in dirs:
            new_r, new_c = x+dr, y+dc
            if new_r < 0 or new_c < 0 or new_r >= len(matrix) or new_c >= len(matrix[0]):
                visited.add((new_r,new_c))
                continue
            if matrix[new_r][new_c] !=9 and (new_r, new_c) not in visited:
                basin_size += 1
                visited.add((new_r, new_c))
                q.append((new_r, new_c))
    return basin_size

basins = []
for r, c in [(r,c) for r in range(len(matrix)) for c in range(len(matrix[0]))]:
    if is_lowpoint(r,c):
        basins.append(bfs(r,c))

basins.sort(reverse=True)
print(basins[0]*basins[1]*basins[2])