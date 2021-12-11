from collections import Counter
import statistics

test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

openers = {"{": "}", "(": ")", "[": "]", "<": ">"}
points = {"}": 1197, ")": 3, "]": 57, ">": 25137}
points_p2 = {")": 1, "]": 2, "}": 3, ">": 4}
expected = []


def syntax_check(line):
    next_char = None

    for i, char in enumerate(line):
        if char in openers:
            next_char = openers[char]
        else:
            if char == next_char:
                line = line[:i-1] + line[i+1:]
                return syntax_check(line)
            else:
                # print(char, next_char)
                # print(f"{i} uhoh {char} expected {next_char}")
                return char
    return line

def part2(string: str) -> int:
    score = 0
    if len(string) == 1:
        return score
    print(string)

    for char in string[::-1]:
        score = (score * 5) + points_p2[openers[char]]
    return score

with open("input") as fh:
    test_input = fh.read()

print(sum((points.get(syntax_check(line), 0) for line in test_input.splitlines())))
print(statistics.median(filter(bool, (part2(syntax_check(line)) for line in test_input.splitlines()))))



