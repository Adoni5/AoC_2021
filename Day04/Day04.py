from collections import defaultdict

test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
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