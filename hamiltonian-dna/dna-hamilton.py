#! /usr/bin/env python3
"""
Nondeterministic algorithm for finding Hamiltonian path in a driected graph.
This is a very bad algorithm which I used only as a reference to compare
against DNA-computing based approach.

L. M. Adleman, Science vol, 266 (1994) - "Molecular Computation of Solutions to Combinatorial Problems"
"""

import random

def generate_random_paths(graph, n_paths):
    random_path_length = random.randint(0, 8)
    paths = []
    for path_id in range(n_paths):
        path = [random.choice(range(6))]

        # random walk in the graph
        while True:
            last = path[-1]
            if len(graph[last]) == 0: break
            path.append(random.choice(graph[last]))

        paths.append(path)
    return paths

def select_by_endpoints(paths, origin, destination):
    return [path for path in paths if path[0] == origin and path[-1] == destination]

def select_by_length(paths, length):
    return [path for path in paths if len(path) == length]

def select_without_duplicates(paths):
    return [path for path in paths if len(path) == len(set(path))]

number_of_vertices = 10

graph = [
  [1, 3, 6],
  [2, 3],
  [1, 3],
  [2, 4],
  [1, 5],
  [1, 2, 6],
  []
]

paths = []
while (len(paths) == 0):
    paths = generate_random_paths(graph, 1)
    paths = select_by_endpoints(paths, 0, 6)
    paths = select_by_length(paths, len(graph))
    paths = select_without_duplicates(paths)

print(paths)
