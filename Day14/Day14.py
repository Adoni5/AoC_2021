import re
from collections import Counter
from itertools import pairwise, chain

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
final_letter = input[-1]
pat = re.compile(r"(\w+) -> (\w)")
templates = {inp: outp for inp, outp in pat.findall(templates)}
input = pairwise(input)
count = Counter("".join(p) for p in input)
for _ in range(40):
    print(_ + 1)
    count2 = Counter()
    for t, v in count.items():
        count2[f"{t[0]}{templates[t]}"] += v
        count2[f"{templates[t]}{t[1]}"] += v
    count = count2
monos = {k for k in chain.from_iterable(count.keys())}
mono_counts = Counter()
for m in monos:
    mono_counts[m] = sum(v for c, v in count.items() if m == c[1])
print(max(mono_counts.values()) - min(mono_counts.values()))