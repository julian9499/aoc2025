from scipy.optimize import linprog, milp, Bounds, LinearConstraint
import numpy as np


def parse_line_part2(line):
    buttons = []
    i = 0
    while i < len(line):
        if line[i] == '(':
            j = line.index(')', i)
            button_str = line[i + 1:j]
            button = list(map(int, button_str.split(',')))
            buttons.append(button)
            i = j + 1
        elif line[i] == '{':
            break
        else:
            i += 1

    jolt_start = line.index('{') + 1
    jolt_end = line.index('}')
    joltages = list(map(int, line[jolt_start:jolt_end].split(',')))

    return buttons, joltages


def min_button_presses(buttons, joltages):
    n_counters = len(joltages)
    n_buttons = len(buttons)

    A = np.zeros((n_counters, n_buttons), dtype=float)
    for j, button in enumerate(buttons):
        for counter in button:
            A[counter][j] = 1

    c = np.ones(n_buttons)

    constraints = LinearConstraint(A, lb=joltages, ub=joltages)

    bounds = Bounds(lb=0, ub=np.inf)

    integrality = np.ones(n_buttons)

    result = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)

    if result.success:
        return int(np.sum(result.x))

    return -1


if __name__ == '__main__':
    inputs = []
    with open("./input", "r") as file:
        inputs = [line.strip() for line in file.readlines()]

    total_presses = 0
    for line in inputs:
        if line:
            print(line)
            buttons, joltages = parse_line_part2(line)
            min_p = min_button_presses(buttons, joltages)
            total_presses += min_p

    print(total_presses)
