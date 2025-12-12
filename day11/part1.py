from collections import defaultdict


def count_paths(graph, start, end):
    count = 0

    def dfs(node):
        nonlocal count
        if node == end:
            count += 1
            return
        for neighbor in graph[node]:
            dfs(neighbor)

    dfs(start)
    return count


if __name__ == '__main__':
    inputs = []
    with open("./input", "r") as file:
        inputs = [line.strip() for line in file.readlines()]

    # Build the graph
    graph = defaultdict(list)
    for line in inputs:
        parts = line.split(": ")
        source = parts[0]
        destinations = parts[1].split()
        graph[source] = destinations

    result = count_paths(graph, "you", "out")
    print(result)
