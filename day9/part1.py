
if __name__ == '__main__':
    inputs = []
    with open("./input", "r") as file:
        inputs = [line.strip() for line in file.readlines()]

    points = []
    for line in inputs:
        x, y = map(int, line.split(','))
        points.append((x, y))

    max_area = 0
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            if x1 != x2 and y1 != y2:
                area = (abs(x2 - x1)+1) * (abs(y2 - y1)+1)
                max_area = max(max_area, area)

    print(max_area)