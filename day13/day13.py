with open("input.txt", "r") as f:
    folding_instructions = False
    instructions = []
    coords = []
    for line in f:
        line = line.strip()
        if line == "":
            folding_instructions=True
            continue
        if folding_instructions:
            instructions.append(line)
        else:
            x,y = line.split(",")
            coords.append((int(x), int(y)))


def fold_up(coords, row):
    new_coords = [(x, y if y < row else row - (y - row)) for x,y in coords]
    return new_coords

def fold_left(coords, col):
    new_coords =[(x if x < col else col - (x - col), y) for x,y in coords]
    return new_coords

coords = fold_left(coords, int(instructions[0].split('=')[1]))

print(len(set(coords)))


# part 2
for instruction in instructions[1:]:
    func, instruction = instruction.split('=')[0][-1], instruction.split('=')[1]
    if func == 'x':
        coords = fold_left(coords, int(instruction))
    else:
        coords = fold_up(coords, int(instruction))

max_x = max(x for x, y in coords)
max_y = max(y for x, y in coords)


for y in range(max_y+1):
    for x in range(max_x+1):
        if (x,y) in coords:
            print("#", end='')
        else:
            print(".", end='')
    print()




