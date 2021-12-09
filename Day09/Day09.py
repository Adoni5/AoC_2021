test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

fw = next((len(line) for line in test_input.splitlines()))
heights = list(map(int, test_input.replace("\n", "")))
neighbours = (-1, +1, fw, fw+1, fw-1, -fw, -fw -1, -fw + 1)
low_points = [x for i, x in enumerate(heights) if all((x < heights[i + n] for n in neighbours if (i + n < len(heights) -1)))]
print(sum(l+1 for l in low_points))
