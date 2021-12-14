import re
from collections import Counter
from itertools import pairwise
test_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
with open("input") as fh:
    test_input = fh.read().strip()
input, templates = test_input.split("\n\n")
pat = re.compile(r"(\w+) -> (\w)")
templates = dict(pat.findall(templates))
for _ in range(10):
    answer = []
    for l1, l2 in pairwise(input):
        answer.append(f"{l1}{templates[f'{l1}{l2}']}")
    input = "".join(answer)
    input += l2
c = Counter(input)
print(max(c.values()) - min(c.values()))