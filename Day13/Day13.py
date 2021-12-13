import re
from itertools import repeat
from pprint import pprint

test_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
with open("input", "r") as fh:
    test_input = fh.read()

dots, folds = test_input.split("\n\n")
pat = re.compile(r"(\d+),(\d+)")
dots = {tuple(map(int, (x, y))) for x, y in pat.findall(dots)}

pat = re.compile(r"([xy])=(\d+)")
post_folds = dots
for axis, fold in pat.findall(folds):
    print(axis, fold)
    if axis == "x":
        print("hello")
        print(sorted(post_folds))
        post_folds = {(abs(x - int(fold)*2) if x > int(fold) else x, y) for x, y in post_folds}
        print("after")
        print(sorted(post_folds))

    else:
        post_folds = {(x, abs(y - int(fold)*2) if y > int(fold) else y) for x, y in post_folds}
    print(sorted(post_folds))


def gmmd(dots, idx):
    for x in dots:
        yield x[idx]


def print_letters(dots):
    """
    Hopefully print our all the letters....
    :param dots:
    :return:
    """


    min_x, max_x, min_y, max_y = min(gmmd(dots, 0)), max(gmmd(dots, 0)), min(gmmd(dots, 1)), max(gmmd(dots, 1))
    row = list(repeat(" ", max_x+1))
    grid = [list(row) for _ in repeat(row, max_y+1)]
    print(f"grid created with {max_x+1} cols and {max_y+1} rows")
    pprint(grid)
    for x, y in dots:
        print(x,y)
        grid[y][x] = "X"
    with open("grid.txt", "w") as fh:
        for line in grid:
            print(line)
            fh.write("".join(line))
            fh.write("\n")



print(post_folds)
print_letters(post_folds)
