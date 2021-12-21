import time
from itertools import combinations_with_replacement, repeat
from typing import List, Tuple

test_input = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""

with open("input") as fh:
    test_input = fh.read().strip()
enhance_me, input_image = test_input.split("\n\n")
enhance_me = enhance_me.replace("\n", "")

def print_grid(grid: List[List]) -> None:
    """
    Print a grid held as a list of lists
    Parameters
    ----------
    grid: list of list

    Returns
    -------
    None

    """
    print("\n".join(["".join(line) for line in grid]))

def get_neighbours(graph: List[List], index: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Get the neighbours of a certain element in the graph
    Parameters
    ----------
    graph: list of list
        List of col values in list of Rows
    index
        Tuple of int, the index in the
    Returns
    -------
    list of int
        List of neighbours
    """
    x = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    neighbours = []
    for shift_x, shift_y in x:
        new_index_x = index[0] + shift_x
        new_index_y = index[1] + shift_y
        neighbours.append((new_index_x, new_index_y))
    return neighbours

grid = [list(line) for line in input_image.splitlines()]
print(f"Grid starts at {len(grid)} lines")

lookup_neighbours = {}


def iterate_grid(grid: List[List], count: int = 1, max_count: int = 2) -> List[List]:
    """
    Iterate grid
    Parameters
    ----------
    grid: list of list
    count: int
        The number of iterations
    max_count: int
        The maximum number of iterations to perform
    Returns
    -------
    list of list
        New bigger grid
    """
    print(f"count {count}")
    t = time.perf_counter()
    for x in range(-1, len(grid[0]) + 1):
        for y in range(-1, len(grid) + 1):
            lookup_neighbours[(y, x)] = get_neighbours(grid, (y, x))
    print(len(lookup_neighbours))

    print(time.perf_counter() - t)
    is_flashed = not count % 2 and enhance_me[0] == "#"
    outside_grid_char = "." if not is_flashed else "#"
    grid_2 = [[] for _ in range(0, len(grid) + 2)]
    for idx, neighbours in lookup_neighbours.items():
        stringy = ""
        for col, row in neighbours:
            next_char = outside_grid_char if any(ni < 0 or ni > len(grid) - 1 for ni in (col, row)) else grid[row][col]
            stringy += next_char
        looky_uppy = {".": "0", "#": "1"}
        stringy = "".join(map(looky_uppy.get, stringy))
        grid_2[idx[1] + 1].append(enhance_me[int(stringy, 2)])
    # print_grid(grid_2)
    print(f"After {count} iteration(s) grid has {len(grid_2)} lines")
    if count < max_count:
        return iterate_grid(grid_2, count=count + 1, max_count=max_count)
    else:
        # print(grid_2)
        return grid_2


if __name__ == "__main__":
    grid = iterate_grid(grid, max_count=50)
    print(grid)
    print("".join(("".join(line) for line in grid)).count("#"))
    # print_grid(grid)



