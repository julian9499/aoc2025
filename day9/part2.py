from collections import deque

if __name__ == '__main__':
    inputs = []
    with open("./input", "r") as file:
        inputs = [line.strip() for line in file.readlines()]

    points = []
    for line in inputs:
        x, y = map(int, line.split(','))
        points.append([x, y])

    x_coords = sorted(set(point[0] for point in points))
    y_coords = sorted(set(point[1] for point in points))

    x_indices = {x: 2 * i + 2 for i, x in enumerate(x_coords)}
    y_indices = {y: 2 * i + 2 for i, y in enumerate(y_coords)}

    grid_size_x = 2 * len(x_coords) + 8
    grid_size_y = 2 * len(y_coords) + 8

    grid = [["?" for _ in range(grid_size_y)] for _ in range(grid_size_x)]

    def fill_line(point, point2):
        min_x = min(point[0], point2[0])
        max_x = max(point[0], point2[0])
        min_y = min(point[1], point2[1])
        max_y = max(point[1], point2[1])
        for x_index in range(x_indices[min_x], x_indices[max_x] + 1):
            for y_index in range(y_indices[min_y], y_indices[max_y] + 1):
                grid[x_index][y_index] = "#"

    for i in range(len(points) - 1):
        fill_line(points[i], points[i + 1])
    fill_line(points[-1], points[0])

    grid[0][0] = "."
    outside_points = deque([[0, 0]])

    while outside_points:
        x, y = outside_points.popleft()
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < grid_size_x and 0 <= ny < grid_size_y:
                    if grid[nx][ny] == "?":
                        grid[nx][ny] = "."
                        outside_points.append([nx, ny])

    def is_filled(point, point2):
        min_x = min(point[0], point2[0])
        max_x = max(point[0], point2[0])
        min_y = min(point[1], point2[1])
        max_y = max(point[1], point2[1])
        for x_index in range(x_indices[min_x], x_indices[max_x] + 1):
            for y_index in range(y_indices[min_y], y_indices[max_y] + 1):
                if grid[x_index][y_index] == ".":
                    return False
        return True

    max_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if is_filled(points[i], points[j]):
                area = (abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1]) + 1)
                max_area = max(max_area, area)

    print(max_area)
