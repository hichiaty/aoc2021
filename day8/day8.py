with open('input.txt') as f:
    data = [i.split(' | ') for i in f.readlines()]

disps = []
for wires, disp in data:
    disps.extend(disp.split())
print(sum(len(x) in (2, 3, 4, 7) for x in disps))

# Part 2
total = 0
for wires, disp in data:
        dispvals = [''.join(sorted(s)) for s in disp.split()]
        digits = {*wires.split(), *dispvals}
        digits = {''.join(sorted(part)) for part in digits}
        num_to_signal = {}
        num_to_signal[1], = (s for s in digits if len(s) == 2)
        num_to_signal[7], = (s for s in digits if len(s) == 3)
        num_to_signal[4], = (s for s in digits if len(s) == 4)
        num_to_signal[8], = (s for s in digits if len(s) == 7)
        len6 = [s for s in digits if len(s) == 6]

        num_to_signal[6], = (s for s in len6 if len(set(s) & set(num_to_signal[1])) == 1)
        num_to_signal[9], = (s for s in len6 if len(set(s) & set(num_to_signal[4])) == 4)
        num_to_signal[0], = set(len6) - {num_to_signal[6], num_to_signal[9]}
        len5 = [s for s in digits if len(s) == 5]

        num_to_signal[5], = (s for s in len5 if len(set(s) & set(num_to_signal[6])) == 5)
        num_to_signal[3], = (s for s in len5 if len(set(s) & set(num_to_signal[1])) == 2)
        num_to_signal[2], = set(len5) - {num_to_signal[5], num_to_signal[3]}
        signal_to_num = {v: k for k, v in num_to_signal.items()}

        total += sum(10 ** (3 - i) * signal_to_num[dispvals[i]] for i in range(len(dispvals)))
print(total)