
with open('input.txt', 'r') as f:
    crabs = [int(i) for i in f.readlines()[0].split(',')]

# just brute force it
possible_targets = range(1,max(crabs)+1)

min_fuel = float('inf')
for target in possible_targets:
    total_fuel = 0
    for crab in crabs:
        total_fuel += abs(target - crab)
    min_fuel = min(min_fuel, total_fuel)

print(min_fuel)

# part 2
possible_targets = range(1,max(crabs)+1)
min_fuel = float('inf')
for target in possible_targets:
    total_fuel = 0
    for crab in crabs:
        total_fuel += sum([i for i in range(1,abs(target - crab)+1)])
    min_fuel = min(min_fuel, total_fuel)

print(min_fuel)