
def max_joltage(bank):
    keep = 2
    k = len(bank) - keep
    stack = []
    for d in bank:
        while k and stack and stack[-1] < d:
            stack.pop()
            k -= 1
        stack.append(d)
    return int(''.join(stack[:keep]))

if __name__ == '__main__':

    inputs = []
    with open("./input", "r") as file:
        inputs = [line.strip() for line in file.readlines()]

        total = sum(max_joltage(bank) for bank in inputs)
        print(total)