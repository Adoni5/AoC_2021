from typing import List
from collections import deque

test_input = """3,4,3,1,2"""

def grow(ages: List, days: int) -> int:
    age_counts = deque([0] * 9)
    for age in ages:
        age_counts[age] += 1

    for i in range(days):
        ageing_up = age_counts.popleft()
        age_counts.append(ageing_up)
        age_counts[6] += ageing_up
    return sum(age_counts)


if __name__ == "__main__":
    with open("input") as fh:
        line = list(map(int, fh.read().split(",")))
        print(f"Part 1: {grow(line, 80)}")
        print(f"Part 2: {grow(line, 256)}")
