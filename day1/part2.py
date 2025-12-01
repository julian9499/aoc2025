
if __name__ == '__main__':
    inputs = []
    with open("./input", "r") as file:
        inputs = [line.strip() for line in file.readlines()]

    ans = 50
    count = 0
    for x in inputs:
        direction = x[0]
        steps = int(x[1:])
        if direction == 'L':
            for i in range(1, steps + 1):
                pos = (ans - i) % 100
                if pos == 0:
                    count += 1
            ans = (ans - steps) % 100
        else:
            for i in range(1, steps + 1):
                pos = (ans + i) % 100
                if pos == 0:
                    count += 1
            ans = (ans + steps) % 100
    print(count)
