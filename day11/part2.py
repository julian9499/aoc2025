from collections import defaultdict
from functools import lru_cache


def count_paths_with_required(graph, start, end, required):
    required_list = list(required)
    required_to_bit = {node: 1 << i for i, node in enumerate(required_list)}
    full_mask = (1 << len(required_list)) - 1

    @lru_cache(maxsize=None)
    def dfs(node, visited_mask):
        if node in required_to_bit:
            visited_mask |= required_to_bit[node]
        if node == end:
            return 1 if visited_mask == full_mask else 0
        total = 0
        for neighbor in graph[node]:
            total += dfs(neighbor, visited_mask)
        return total

    for key in graph:
        graph[key] = tuple(graph[key])

    return dfs(start, 0)


if __name__ == '__main__':
    with open("./input", "r") as file:
        inputs = [line.strip() for line in file.readlines()]

    graph = defaultdict(tuple)
    for line in inputs:
        parts = line.split(": ")
        source = parts[0]
        destinations = tuple(parts[1].split())
        graph[source] = destinations

    required_nodes = {"dac", "fft"}
    result = count_paths_with_required(graph, "svr", "out", required_nodes)
    print(result)
