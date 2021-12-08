import re
from collections import Counter, defaultdict

test_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

with open("input") as fh:
    test_input = fh.read()

pat = re.compile(r"(?:\|\n|\| )(\w+) (\w+) (\w+) (\w+)")

c = Counter()
digits = pat.findall(test_input)
for digit in digits:
    for digi in digit:
        c[len(digi)] += 1

print(sum((c[i] for i in {2, 4, 3, 7})))


def get_digit(digit: str, lookup: dict) -> str:
    return str(lookup["".join(sorted(digit))])

# part 2
county = 0
for line in test_input.splitlines():
    top = set()
    mid = set()
    bot = set()
    tr = set()
    tl = set()
    br = set()
    bl = set()
    pat = re.compile(r"(\w+)")
    words = pat.findall(line)
    signals = words[:10]
    code = words[-4:]
    letters2num = {}
    num_code_holder = defaultdict(list)
    for num_code in words:
        num_code_holder[len(num_code)].append(set(num_code))
    tr.update(num_code_holder[2][0])
    br.update(num_code_holder[2][0])
    top.update(num_code_holder[3][0] - num_code_holder[2][0])
    mid.update(num_code_holder[4][0] - num_code_holder[2][0])
    tl.update(num_code_holder[4][0] - num_code_holder[2][0])
    bl.update(num_code_holder[7][0] - top - tr - tl)
    # fivey = None
    letters2num["".join(sorted(num_code_holder[3][0]))] = 7
    letters2num["".join(sorted(num_code_holder[2][0]))] = 1
    letters2num["".join(sorted(num_code_holder[7][0]))] = 8
    letters2num["".join(sorted(num_code_holder[4][0]))] = 4
    for num_code in num_code_holder[5]:
        if len(num_code.intersection(tl)) == 2:
            letters2num["".join(sorted(num_code))] = 5
            fivey = num_code
        elif len(num_code.intersection(bl)) == 2:
            letters2num["".join(sorted(num_code))] = 2
        else:
            letters2num["".join(sorted(num_code))] = 3
    for num_code in num_code_holder[6]:
        if len(num_code.intersection(tr)) == 1:
            letters2num["".join(sorted(num_code))] = 6
        elif len(num_code.intersection(tr)) == 2 and len(num_code.intersection(bl)) == 2:
            letters2num["".join(sorted(num_code))] = 0
        else:
            letters2num["".join(sorted(num_code))] = 9
    county += int("".join(get_digit(c, letters2num) for c in code))
print(county)

# tl = fivey - num_code_holder[5][0] - num_code_holder[5][1]
# mid = mid - tl
# tr = tr - tr.intersection(num_code)
# br = br - tr
# bot = num_code - top - tl - mid - br
# bl = num_code_holder[7][0] - num_code - tr



