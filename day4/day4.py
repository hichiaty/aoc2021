with open('input.txt', 'r') as f:
    lines = f.readlines()

calls = lines[0].strip().split(',')
boards = []
curboard = []
for line in lines[2:]:
    if line.strip() != '':
        curboard.append(line.strip().split())
    else:
        boards.append(curboard)
        curboard = []


def mark_boards(boards, call):
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            for col in range(len(boards[board][row])):
                if boards[board][row][col] == call:
                    boards[board][row][col] = 'X'
    return boards

def check_board(board):
    rows = board
    columns = list(zip(*board))
    for row in rows:
        if all([i == 'X' for i in row]):
            return True
    for column in columns:
        if all([i == 'X' for i in column]):
            return True
    return False

def get_sum(board):
    sum = 0
    for row in board:
        for i in row:
            if i != 'X':
                sum += int(i)
    return sum

# find first winning board
found = False
for call in calls:
    if found:
        break
    boards = mark_boards(boards, call)
    for board in boards:
        if check_board(board):
            print(int(call)*get_sum(board))
            found = True
            break

# find last winning board
calls = lines[0].strip().split(',')
boards = []
curboard = []
for line in lines[2:]:
    if line.strip() != '':
        curboard.append(line.strip().split())
    else:
        boards.append(curboard)
        curboard = []

last_winner = None
seen_boards = []
for call in calls:
    boards = mark_boards(boards, call)
    for board in boards:
        if board not in seen_boards:
            if check_board(board):
                last_winner = int(call)*get_sum(board)
                seen_boards.append(board)
print(last_winner)