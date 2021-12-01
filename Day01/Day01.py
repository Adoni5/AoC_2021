from collections import deque

test_input = """199
200
208
210
200
207
240
269
260
263"""


def part1(input: str) -> int:
    deeper_count = 0
    prev = None
    input = map(int, input.split("\n"))
    for depth in input:
        if not prev:
            prev = depth
            continue
        if prev < depth:
            deeper_count += 1
        prev = depth
    return deeper_count

# def part2(input: str) -> int:





if __name__ == "__main__":
    assert part1(test_input) == 7, "Test part 01"
    with open("input", "r") as fh:
        input = fh.read().strip()
        print(part1(input))
        deeper_count = 0
        inputty = map(int, input.split("\n"))
        depths_windows = deque(maxlen=3)
        deeper_count = 0
        prev = None
        for depth in inputty:
            depths_windows.append(depth)
            if not len(depths_windows) == 3:
                continue
            summed_depth = sum(depths_windows)
            if not prev:
                prev = summed_depth
                continue
            if summed_depth > prev:
                deeper_count += 1
            prev = summed_depth
        print(deeper_count)