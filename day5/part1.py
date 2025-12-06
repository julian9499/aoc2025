if __name__ == '__main__':
    lines = []
    with open("./input", "r") as file:
        lines = [line.strip() for line in file.readlines()]

separator_index = lines.index('')

ranges = []
for line in lines[:separator_index]:
    start, end = line.split('-')
    ranges.append([int(start), int(end)])

ids = [int(line) for line in lines[separator_index + 1:]]
ranges = sorted(ranges, key=lambda x: x[0])
stack = [ranges[0]]
for r in ranges[1:]:
    if r[0] > stack[-1][1]:
        stack.append(r)
    else:
        p = stack.pop()
        stack.append((min(p[0], r[0]), max(p[1], r[1])))
print("Total fresh IDs:", sum([r[1]-r[0]+1 for r in stack]))

valid_ids = 0
for id in ids:
    for i in stack:
        if id in range(i[0], i[1]+1):
            valid_ids += 1
            break
print("valid IDs:", valid_ids)
