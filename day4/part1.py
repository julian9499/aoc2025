


if __name__ == '__main__':

    inputs = []
    grid_count=[]
    with open("./input", "r") as file:
        inputs = [list(line.strip()) for line in file.readlines()]

    for x in range(len(inputs)):
        grid_count.append([])
        for y in range(len(inputs[x])):
            grid_count[x].append(0)
            count = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0: continue
                    if x+i < 0 or x+i >= len(inputs) or y+j < 0 or y+j >= len(inputs[x]): continue
                    if inputs[x+i][y+j] == '@': count += 1
            grid_count[x][y] = count if inputs[x][y] == '@' else 10

    total_count = 0
    for x in grid_count:
        for y in x:
            if y < 4:
                total_count += 1

    print(total_count)

