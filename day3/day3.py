with open('input.txt', 'r') as f:
    data = f.readlines()
    zero_count = [0]*len(data[0].strip())
    one_count = [0]*len(data[0].strip())
    for line in data:
        line = line.strip()
        for i in range(len(line)):
            if line[i] == '0':
                zero_count[i] += 1
            if line[i] == '1':
                one_count[i] += 1
gamma_rate = ''
epsilon_rate = ''

for count0,count1 in zip(zero_count,one_count):
    most_common = 0 if count0 > count1 else 1
    least_common = 1 if count0 > count1 else 0
    gamma_rate += str(most_common)
    epsilon_rate += str(least_common)

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

print(gamma_rate*epsilon_rate)

def get_most_common(listofbinary, idx):
    zero_count = 0
    one_count = 0
    for line in listofbinary:
        if line[idx] == '0':
            zero_count += 1
        if line[idx] == '1':
            one_count += 1
    return 0 if zero_count > one_count else 1

def get_least_common(listofbinary, idx):
    zero_count = 0
    one_count = 0
    for line in listofbinary:
        if line[idx] == '0':
            zero_count += 1
        if line[idx] == '1':
            one_count += 1
    return 1 if zero_count > one_count else 0

# oxygen rating
criteria_numbers = data.copy()
bit_idx = 0
while len(criteria_numbers)>1 and bit_idx<=len(criteria_numbers[0])-1:
    most_common = get_most_common(criteria_numbers, bit_idx)
    criteria_numbers = [x for x in criteria_numbers if x[bit_idx] == str(most_common)]
    bit_idx += 1
oxygen_rating = int(criteria_numbers[0], 2)
# co2 rating
criteria_numbers = data.copy()
bit_idx = 0
while len(criteria_numbers)>1 and bit_idx<=len(criteria_numbers[0])-1:
    least_common = get_least_common(criteria_numbers, bit_idx)
    criteria_numbers = [x for x in criteria_numbers if x[bit_idx] == str(least_common)]
    bit_idx += 1
co2_rating = int(criteria_numbers[0], 2)

print(oxygen_rating*co2_rating)