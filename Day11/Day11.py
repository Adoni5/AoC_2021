import numpy as np
test_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

with open("input") as fh:
    test_input = fh.read()

arr = np.array([list(map(int, line)) for line in test_input.splitlines()])

summy = 0
for _ in range(10000):
    arr += 1
    flash = arr[arr > 9].any()
    zero_me = []
    while flash:
        x, y = np.where(arr > 9)
        for x1, y1 in zip(x, y):
            x2 = x1 - 1 if x1 != 0 else 0
            y2 = y1 - 1 if y1 != 0 else 0
            arr[x2:x1 + 2, y2:y1 + 2] += 1
            arr[x1,y1] = 0
            zero_me.append((x1, y1))
        flash = arr[arr > 9].any()
    for x, y in zero_me:
        arr[x, y] = 0
    summy += arr[arr == 0].size
    if arr[arr == 0].size == 100:
        print(_ + 1)
        break

