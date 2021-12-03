with open('input.txt', 'r') as f:
    data = [int(i.strip()) for i in f.readlines()]

increases = 0
for i in range(1,len(data)):
    if data[i] > data[i-1]:
        increases += 1
print(increases)

increases = 0
for i in range(2,len(data)-1):
    if sum(data[i-2:i+1]) < sum(data[i-1:i+2]):
        increases += 1
print(increases)