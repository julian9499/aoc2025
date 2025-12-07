from collections import deque


def count_splits(grid):
    rows, cols = len(grid), len(grid[0])

    for c in range(cols):
        if grid[0][c] == 'S':
            start = (0, c)
            break

    queue = deque()
    visited = set()
    splits = 0

    queue.append((start[0] + 1, start[1]))

    while queue:
        r, c = queue.popleft()
        if not (0 <= r < rows and 0 <= c < cols):
            continue
        if (r, c) in visited:
            continue
        visited.add((r, c))

        cell = grid[r][c]
        if cell == '.':
            queue.append((r + 1, c))
        elif cell == '^':
            splits += 1
            if c - 1 >= 0:
                queue.append((r + 1, c - 1))
            if c + 1 < cols:
                queue.append((r + 1, c + 1))

    return splits

if __name__ == '__main__':
    with open('./input', 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    print(count_splits(grid))
