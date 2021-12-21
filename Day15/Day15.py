import time
from itertools import repeat
from pprint import pprint
from typing import List, Tuple
import heapq

import numpy as np

test_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
with open("input") as fh:
    test_input = fh.read().strip()

graph = [list(map(int, line)) for line in test_input.splitlines()]
# print("\n".join(["".join(map(str, s)) for s in graph]))
# print(len(graph))

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
    x = (-1, 1)
    neighbours = set()
    for shift in x:
        if abs(index[0] + shift) < len(graph[0]):
            new_index_x = (abs(index[0] + shift), index[1],)
            neighbours.add(new_index_x)
        if abs(index[1] + shift) < len(graph):
            new_index_y = (index[0], abs(index[1] + shift))
            neighbours.add(new_index_y)
    return list(neighbours)

lookup = {}
t = time.perf_counter()
for i in range(len(graph)):
    for j in range(len(graph[0])):
        lookup[(i, j)] = get_neighbours(graph, (i, j))
print(time.perf_counter() - t)

visited = {(0,0)}
risk = 0
heapy = [(risk, (0, 0))]
len_col, len_row = len(graph[0]) - 1, len(graph) - 1
while heapy:
    risk, (x, y) = heapq.heappop(heapy)
    if (x, y) == (len_col, len_row):
        print(risk)
        break
    neighbours = lookup[(x, y)]
    # print(f"looking at {x, y}")
    # print(f"neighbours are {neighbours}")
    for col, row in neighbours:
        if (col, row) not in visited:
            visited.add((col, row))
            # print(f"looking at neighbouring index {col, row}")
            # print(f"risk is {graph[row][col]}")
            heapq.heappush(heapy, (risk + graph[row][col], (col, row)))
            # print(f"current paths are {heapy}\n")
grids = []

for i in range(5):
    row_of_tiles = []
    for j in range(i, 5+i):
        grid = np.array(graph) + j
        grid[np.where(grid > 9)] = grid[np.where(grid > 9)] % 9
        row_of_tiles.append(grid.tolist())
    grids.append(np.concatenate(row_of_tiles, axis=1))
graph = np.concatenate(grids).tolist()

lookup = {}
t = time.perf_counter()
for i in range(len(graph)):
    for j in range(len(graph[0])):
        lookup[(i, j)] = get_neighbours(graph, (i, j))
print(time.perf_counter() - t)

visited = {(0,0)}
risk = 0
heapy = [(risk, (0, 0))]
len_col, len_row = len(graph[0]) - 1, len(graph) - 1
while heapy:
    risk, (x, y) = heapq.heappop(heapy)
    if (x, y) == (len_col, len_row):
        print(risk)
        break
    neighbours = lookup[(x, y)]
    # print(f"looking at {x, y}")
    # print(f"neighbours are {neighbours}")
    for col, row in neighbours:
        if (col, row) not in visited:
            visited.add((col, row))
            # print(f"looking at neighbouring index {col, row}")
            # print(f"risk is {graph[row][col]}")
            heapq.heappush(heapy, (risk + graph[row][col], (col, row)))
            # print(f"current paths are {heapy}\n")




