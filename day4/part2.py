
def update_grid(inputs):
    grid_count=[]

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
    for x in range(len(grid_count)):
        for y in range(len(grid_count[x])):
            if grid_count[x][y] < 4:
                total_count += 1
                inputs[x][y] = '.'
    return total_count, inputs

if __name__ == '__main__':

    inputs = []
    with open("./input", "r") as file:
        inputs = [list(line.strip()) for line in file.readlines()]

    prev_count = -1
    total_count = 0
    while prev_count != total_count:
        prev_count = total_count
        count, inputs = update_grid(inputs)
        total_count += count

    print(total_count)

