import collections

with open('input.txt', 'r') as f:
    fishes = [int(i) for i in f.readlines()[0].split(',')]

for day in range(80):
    for i in range(len(fishes)):
        if fishes[i]!=0:
            fishes[i]-=1
        else:
            fishes[i] = 6
            fishes.append(8)
print(len(fishes))

with open('input.txt', 'r') as f:
    fishes = [int(i) for i in f.readlines()[0].split(',')]


fishes = collections.Counter(fishes)
for day in range(256):
    newfish = collections.Counter({8: fishes[0], 6: fishes[0]})
    newfish.update({k - 1: v for k, v in fishes.items() if k > 0})
    fishes = newfish
print(sum(fishes.values()))