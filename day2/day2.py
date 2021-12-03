horizontal = 0
depth = 0

with open('input.txt', 'r') as f:
    for line in f:
        action, amount = line.strip().split()
        if action == 'forward':
            horizontal += int(amount)
        elif action == 'up':
            depth -= int(amount)
        elif action == 'down':
            depth += int(amount)
print(horizontal*depth)


horizontal = 0
depth = 0
aim = 0
with open('input.txt', 'r') as f:
    for line in f:
        action, amount = line.strip().split()
        if action == 'forward':
            horizontal += int(amount)
            depth -= int(amount)*aim
        elif action == 'up':
            aim += int(amount)
        elif action == 'down':
            aim -= int(amount)

print(horizontal*depth)