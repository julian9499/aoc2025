from collections import defaultdict

def count_timelines(grid):
    rows, cols = len(grid), len(grid[0])

    for c in range(cols):
        if grid[0][c] == 'S':
            start = (0, c)
            break

    dp = defaultdict(int)
    dp[start] = 1

    for r in range(rows):
        next_dp = defaultdict(int)
        for c in range(cols):
            if dp[(r, c)] == 0:
                continue

            paths = dp[(r, c)]
            cell = grid[r][c]

            if r == rows - 1:
                # Count these paths as complete timelines
                continue

            if cell == '.' or cell == 'S':
                next_dp[(r + 1, c)] += paths
            elif cell == '^':
                if c - 1 >= 0:
                    next_dp[(r + 1, c - 1)] += paths
                if c + 1 < cols:
                    next_dp[(r + 1, c + 1)] += paths

        dp.update(next_dp)

    return sum(dp[(rows - 1, c)] for c in range(cols))


if __name__ == '__main__':
    with open('./input', 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    print(count_timelines(grid))
