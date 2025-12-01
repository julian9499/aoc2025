

if __name__ == '__main__':

    inputs = []
    with open("./input", "r") as file:
        inputs = [line.strip() for line in file.readlines()]

    ans = 50
    count = 0
    for x in inputs:
        if x[0] =='L':
            ans -= int(x[1:])
        else:
            ans += int(x[1:])
        ans = ans % 100
        if ans == 0:
            count += 1
    print(count)