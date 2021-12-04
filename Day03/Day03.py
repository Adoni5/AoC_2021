from collections import Counter

import pandas as pd

test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

def part01(test_input: str) -> None:
    df = pd.DataFrame((list(bin_str) for bin_str in test_input.splitlines()))
    most_common = "".join(i for i in df.apply(lambda x: x.mode().iloc[0]))
    gamma = int(most_common, 2)
    epsilon = int("".join((str(int(not x)) for x in map(int, most_common))), 2)
    print(gamma * epsilon)


def part02(test_input: str, index: int, co2: bool = True) -> str:
    c = Counter((line[index] for line in test_input.splitlines()))
    x = c.most_common(2)
    x.sort(key=lambda z: (z[1], z[0]), reverse=True)
    letter_to_keep = x[int(co2)][0]
    test_input = "\n".join(line for line in test_input.splitlines() if line[index] == letter_to_keep)
    new_index = index +1
    if not new_index == len(test_input.splitlines()[0]) and not len(test_input.splitlines()) == 1:
        return part02(test_input, new_index, co2)
    else:
        print(f"final test {test_input}")
        return test_input

if __name__ == "__main__":
    with open("input", "r") as fh:
        puz_input = fh.read()
        part01(puz_input)
        o2 = part02(puz_input, 0, False)
        co2 = part02(puz_input, 0, True)
        print(int(o2, 2) * int(co2, 2))


