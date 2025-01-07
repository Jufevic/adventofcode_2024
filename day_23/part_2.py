from pathlib import Path
from collections import defaultdict
import networkx as nx

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

graph = defaultdict(set)

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        first, second = line.split("-")
        graph[first].add(second)
        graph[second].add(first)

G = nx.Graph(graph)
largest_set = max(nx.algorithms.clique.find_cliques(G), key=len)
print(",".join(sorted(largest_set)))
