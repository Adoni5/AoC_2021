import re
from collections import Counter
test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

with open("input", "r") as fh:
    test_input = fh.read().strip()
points_p1 = []
points_p2 = []
pattern = re.compile(r"^(\d+),(\d+).{4}(\d+),(\d+)")
for line in test_input.splitlines():
    x1, y1, x2, y2 = list(map(int, pattern.findall(line)[0]))
    if x1 == x2:
        pointsy_x = [(x1, p1) for p1 in range(min(y1, y2), max(y1, y2) + 1)]
        points_p1.extend(pointsy_x)
        points_p2.extend(pointsy_x)
    elif y1 == y2:
        pointsy_y = [(p1, y1) for p1 in range(min(x1, x2), max(x1, x2) + 1)]
        points_p1.extend(pointsy_y)
        points_p2.extend(pointsy_y)
    else:
        step_x = 1 if x1 < x2 else - 1
        x_coords = range(x1, x2 + step_x, step_x)
        step_y = 1 if y1 < y2 else - 1
        y_coords = range(y1, y2+step_y, step_y)
        pointsy_xy = list(zip(x_coords, y_coords))
        points_p2.extend(pointsy_xy)

c = Counter(points_p1)
c2 = Counter(points_p2)
print(sum((bool(x) for x in c.values() if x > 1)))
print(sum((bool(x) for x in c2.values() if x > 1)))
