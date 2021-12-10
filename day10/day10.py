with open('input.txt', 'r') as f:
    input = f.readlines()

open_to_close = {'{': '}', '[': ']', '(': ')', '<': '>'}
close_to_open = {v: k for k, v in open_to_close.items()}



total = 0
points= { ')': 3, ']': 57, '}': 1197, '>': 25137}

for chunk in input:
    stack = []
    for char in chunk:
        if char in open_to_close:
            stack.append(char)
        elif char in close_to_open:
            if stack[-1] == close_to_open[char]:
                stack.pop()
            else:
                total += points[char]
                break
                
print(total)      

# part 2   
totals = []
points= { ')': 1, ']': 2, '}': 3, '>': 4}
for chunk in input:
    stack = []
    corrupt = False
    for char in chunk:
        if char in open_to_close:
            stack.append(char)
        elif char in close_to_open:
            if stack[-1] == close_to_open[char]:
                stack.pop()
            else:
                corrupt = True
                break
    if not corrupt:
        closing = [open_to_close[i] for i in reversed(stack)]
        score = 0
        for bracket in closing:
            score *= 5
            score += points[bracket]
        totals.append(score)

totals.sort()
print(totals[len(totals)//2])



