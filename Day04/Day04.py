from collections import defaultdict
with open("input") as fh:
    sections = fh.read().strip().split("\n\n")
# sections = test_input.split("\n\n")
drawn_numbers = sections[0]
boards = [board.split("\n") for board in sections[1:]]
rows = {}
cols = defaultdict(set)
for i, board in enumerate(boards):
    for j, row in enumerate(board):
        rowy = [int(x) for x in row.split(" ") if x.isdigit()]
        # boards[i][j] = set(rowy)
        rows[f"{i}{j}"] = set(rowy)
        for col_idx in range(len(rowy)):
            cols[f"{i}{col_idx}"].add(rowy[col_idx])

drawny = set()
board_win_order = {}
for drawn in drawn_numbers.split(","):
    drawny.add(int(drawn))
    for key, col in cols.items():
        if len(col.intersection(drawny)) == 5:
            if not int(key[:-1]) + 1 in board_win_order:
                board_win_order[int(key[:-1]) + 1] = (col, key, True, int(key[:-1]), list(drawny), int(drawn))
            answer = sum([x for k, col in cols.items() if k[:-1] == key[:-1] and not k[-1] == key[-1] for x in col if
                       x not in drawny]) * int(drawn)

    for key, row in rows.items():
        if len(row.intersection(drawny)) == 5:
            if not int(key[:-1]) + 1 in board_win_order:
                board_win_order[int(key[:-1]) + 1] = (row, key, False, int(key[:-1]), list(drawny), int(drawn))
            answer = sum([x for k, row in rows.items() if k[:-1] == key[:-1] and not k[-1] == key[-1] for x in row if x not in drawny]) * int(drawn)

# part 2
last_board = board_win_order[next(reversed(board_win_order))]
step_1 = [int(x) for row in boards[last_board[3]] for x in row.split(" ") if x.isdigit()]
print(sum(x for x in step_1 if x not in last_board[4]) * last_board[-1])