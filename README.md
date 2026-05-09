# 🔍 Graph & Grid Algorithm Library

![MIT License](https://img.shields.io/badge/license-MIT-green.svg) ![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg) ![No dependencies](https://img.shields.io/badge/dependencies-none-brightgreen.svg)

A clean, dependency-free Python library for common **BFS**, **DFS**, and **grid traversal** algorithms. Designed as a reliable toolkit for competitive programming, interview prep, and educational use.

---

## 📥 Installation

```bash
pip install graph-algs
```

Then import directly from the top-level package — no need to reference internal subfolders:

```python
from graph_lib import shortest_path, bfs, lee_algorithm, has_cycle_directed
```

---

## 📦 Modules

```
graph_algorithms/
├── bfs/
│   ├── bfs_general_lib.py      # BFS traversal and shortest paths
│   ├── bfs_undirected_lib.py   # Connectivity for undirected graphs
│   ├── bfs_directed_lib.py     # Weak connectivity for directed graphs
│   └── grid_bfs_lib.py         # Grid BFS — islands, pathfinding, distance problems
└── dfs/
    ├── dfs_general_lib.py      # DFS traversal
    ├── dfs_undirected_lib.py   # Cycle detection for undirected graphs
    └── dfs_directed_lib.py     # Cycle detection for directed graphs
```

---

## ⚙️ Implementation Conventions

Understanding these conventions is essential for using the library correctly.

### Error Handling — Exceptions

All functions raise exceptions on invalid or degenerate input rather than returning a sentinel value:

- **`ValueError`** — empty graph or grid (`{}`, `[]`), invalid board size (`n <= 0`)
- **`KeyError`** — `start`/`end` node not present in the graph, out-of-bounds grid coordinates, start or end cell being a wall

```python
bfs({}, 'A')                        # → ValueError: Graph is empty!
bfs(graph, 'Z')                     # → KeyError: Vertex Z not in graph!
lee_algorithm(grid, (0,0), (9,9))   # → KeyError: (0, 0) or (9, 9) cell not in grid!
count_islands([])                   # → ValueError: Grid is empty!
```

### No Path / No Result — `None`

When inputs are structurally valid but the goal is **unreachable**, functions return **`None`**:

```python
shortest_path(graph, 'A', 'Z')       # → None  (Z unreachable from A)
lee_algorithm(grid, (0,0), (3,3))    # → None  (blocked)
rotting_oranges(grid)                # → None  (some fresh oranges can never rot)
```

### Input Validation Scope

The library performs **only semantic validation** — it checks whether inputs make sense for the algorithm, not whether they conform to a type contract.

✅ **Checked:**
- Whether the graph or grid is empty
- Whether `start`/`end` nodes exist in the graph
- Whether grid coordinates are in bounds
- Whether start/end cells are traversable (value `0`)
- Whether board size is positive (knight moves)

❌ **Not checked:**
- Whether `graph` is actually a `dict`
- Whether grid rows are all the same length
- Whether node values are hashable
- Whether `start`/`end` are tuples vs. lists in grid functions

If you pass malformed data (e.g., a list instead of a dict, or a grid with jagged rows), you will get a native Python exception.

---

## 📖 API Reference

### `bfs/bfs_general_lib.py`

#### Basic Traversal

```python
bfs(graph, start, visited=None) → set
```
Returns the set of all nodes reachable from `start`. Accepts an optional `visited` set to continue a traversal across multiple calls.

```python
bfs_order(graph, start, visited=None) → list
```
Returns nodes in BFS visit order. Accepts an optional shared `visited` set.

```python
bfs_count(graph, start, visited=None) → int
```
Returns the count of nodes reachable from `start`. Accepts an optional shared `visited` set.

```python
bfs_distances(graph, start) → dict
```
Returns a dictionary mapping each reachable node to its shortest distance (in number of edges) from `start`.

#### Shortest Paths

```python
shortest_path(graph, start, end) → list | None
```
Returns the shortest path as a node list. Returns `[start]` if `start == end`. Returns `None` if no path exists.

```python
shortest_path_len(graph, start, end) → int | None
```
Returns the length (number of edges) of the shortest path. Returns `0` if `start == end`. Returns `None` if no path exists.

---

### `bfs/bfs_undirected_lib.py`

```python
is_connected_undirected(graph) → bool
```
Returns `True` if the undirected graph is connected.

```python
count_components_undirected(graph) → int
```
Returns the number of connected components.

```python
get_components_order_undirected(graph) → list[list]
```
Returns a list of components, each as an ordered BFS traversal list.

```python
largest_component_size_undirected(graph) → int
```
Returns the size of the largest component.

```python
shortest_path_len_undirected(graph, start, end) → int | None
```
Faster shortest path length using bidirectional BFS. Requires both `start` and `end` to be present in the graph. Returns `None` if no path exists.

---

### `bfs/bfs_directed_lib.py`

Connectivity functions for directed graphs use **weak connectivity** — the graph is normalised to undirected via `normalize()` before traversal.

```python
normalize(graph) → dict
```
Converts a directed graph into an undirected one by adding reverse edges. Used internally; safe to call directly.

```python
is_connected_directed(graph) → bool
```
Returns `True` if the directed graph is weakly connected.

```python
count_components_directed(graph) → int
```
Returns the number of weakly connected components.

```python
get_components_order_directed(graph) → list[list]
```
Returns a list of weakly connected components, each as an ordered BFS traversal list.

```python
largest_component_size_directed(graph) → int
```
Returns the size of the largest weakly connected component.

---

### `dfs/dfs_general_lib.py`

```python
dfs(graph, start, visited=None) → set
```
Recursive DFS. Returns the set of all visited nodes. Accepts an optional shared `visited` set.

```python
dfs_order(graph, start, visited=None) → list
```
Iterative DFS using an explicit stack. Returns nodes in DFS visit order. Accepts an optional shared `visited` set.

---

### `dfs/dfs_undirected_lib.py`

```python
has_cycle_undirected(graph) → bool
```
Detects cycles in an **undirected** graph using parent tracking.

---

### `dfs/dfs_directed_lib.py`

```python
has_cycle_directed(graph) → bool
```
Detects cycles in a **directed** graph using the white/gray/black coloring method.

---

### `bfs/grid_bfs_lib.py`

> Grid convention: `0` = traversable cell, `1` = wall/obstacle (except `dist_to_nearest_one` and `rotting_oranges` which use domain-specific values).

#### Island Problems

```python
count_islands(grid) → int
```
Counts the number of connected regions of `0`-cells (4-directional).

```python
get_islands_order(grid) → list[list[tuple]]
```
Returns all islands as lists of `(row, col)` coordinates in BFS order.

```python
largest_island_area(grid) → int
```
Returns the cell count of the largest island.

#### Pathfinding (Lee Algorithm)

```python
lee_algorithm(grid, start, end) → list[tuple] | None
```
Finds the shortest path in a grid from `start` to `end`. Returns path as a list of `(row, col)` tuples. Returns `None` if unreachable.

```python
lee_algorithm_len(grid, start, end) → int | None
```
Returns the length of the shortest grid path. Returns `0` if `start == end`. Returns `None` if unreachable.

#### Distance & Simulation

```python
dist_to_nearest_one(grid) → list[list[int]]
```
Multi-source BFS. Returns a grid where each cell contains its distance to the nearest `1`-cell. Cells that are `1` have distance `0`.

```python
rotting_oranges(grid) → int | None
```
Simulates rotting spread (LeetCode 994). Grid values: `0` = empty, `1` = fresh orange, `2` = rotten orange. Returns minutes until all oranges rot, or `None` if impossible.

#### Knight Moves

```python
knight_moves(n, start, end) → list[tuple] | None
```
Finds the shortest path for a chess knight on an `n×n` board. Returns path as `(row, col)` tuples. Returns `None` if unreachable.

```python
knight_moves_len(n, start, end) → int | None
```
Returns the minimum number of moves for a knight to travel from `start` to `end`. Returns `None` if unreachable.

---

## 🗺️ Graph Format

All graph functions expect an **adjacency list** as a Python `dict`.

### Implicit sink nodes in directed graphs

In a directed graph, nodes that have **no outgoing edges** don't have to appear as explicit keys — they can exist only as values in other nodes' neighbour lists. This is supported via `graph.get(node, [])` instead of `graph[node]` everywhere neighbours are iterated, so a missing key is safely treated as having no outgoing edges.

```python
# ✅ Both forms are equivalent and accepted

# Explicit — sink nodes listed with empty neighbour lists
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],       # sink, explicitly listed
    'D': []        # sink, explicitly listed
}

# Compact — sink nodes omitted as keys entirely
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    # C and D are implied by appearing in neighbour lists
}
```

> ⚠️ **Exception:** functions that validate `start` by checking `if start not in graph` will raise `KeyError` if a sink node is passed as `start` and is not an explicit key. If you need to start traversal from a sink, include it explicitly with an empty list.

For undirected graphs, all edges must still be listed in both directions:

```python
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}
```

Nodes can be any hashable type (strings, integers, tuples, etc.).

## 🗺️ Grid Format

Grid functions expect a **2D list of integers**:

```python
grid = [
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 0],
]
```

Coordinates are always `(row, col)`. All movement is **4-directional** (up, down, left, right).

---

## 💡 Usage Examples

```python
from graph_lib import (
    shortest_path, bfs_distances, count_components_undirected, count_components_directed,
    dfs_order, has_cycle_directed, has_cycle_undirected,
    lee_algorithm, rotting_oranges
)

# Shortest path in an undirected graph
graph = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}
print(shortest_path(graph, 1, 4))  # → [1, 2, 4]

# Get distances from a start node
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
print(bfs_distances(graph, 'A'))  # → {'A': 0, 'B': 1, 'C': 1, 'D': 2}

# Count weakly connected components in a directed graph
dgraph = {'A': ['B'], 'B': [], 'C': ['D'], 'D': []}
print(count_components_directed(dgraph))  # → 2

# Count connected components in an undirected graph
ugraph = {1: [2], 2: [1], 3: [4], 4: [3]}
print(count_components_undirected(ugraph))  # → 2

# Cycle detection
print(has_cycle_directed({'A': ['B'], 'B': ['A']}))        # → True
print(has_cycle_undirected({1: [2], 2: [1, 3], 3: [2]}))  # → False

# Grid shortest path
grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
print(lee_algorithm(grid, (0, 0), (2, 2)))  # → [(0,0), (0,1), (0,2), (1,2), (2,2)]

# Rotting oranges
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(rotting_oranges(grid))  # → 4
```

---

## 📌 Quick Reference: Return Values

| Situation | Return Value |
|-----------|-------------|
| Invalid / empty input | `ValueError` or `KeyError` |
| Valid input, goal unreachable | `None` |
| `start == end` (path functions) | `[start]` or `0` |
| Success | Result value or list (dict) |

---

<p align="center">Made with ❤️ and Python</p>
