import re
test_input = """target area: x=20..30, y=-10..-5"""
with open("input") as fh:
    test_input = fh.read().strip()
pat = re.compile(r"x=(\d+)..(\d+), y=(-\d+)..(-\d+)")
x1, x2, y2, y1 = map(int, pat.findall(test_input)[0])


def step(start_traj, target):
    """
    Step the arc forward one
    :param start_traj:
    :return:
    """
    x1, x2, y1, y2 = target
    traj = list(start_traj)
    point = [0,0]
    max_y = 0
    while point[0] <= x2 and point[1] >= y2:
        point[0] += traj[0]
        point[1] += traj[1]
        if point[1] > max_y:
            max_y = point[1]
        if all((x2 >= point[0] >= x1, y1 >= point[1] >= y2)):
            return (start_traj, max_y)
        elif (any((point[0] > x2, point[1]<y2))):
            return ((0, 0), 0)
        if traj[0] > 0:
            traj[0] -= 1
        traj[1] -= 1
hits = []
for xv in range(1, x2 + 1):
    for yv in range(y2,abs(y2) +1):
        # print(f"Initial {xv, yv}")
        hits.append(step([xv, yv], (x1, x2, y1, y2)))

print(max(max_y[1] for max_y in hits))
print(len(list(filter(lambda x: bool(x[0][0]), hits))))

