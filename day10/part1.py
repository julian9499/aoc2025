from collections import deque


def parse_line(line):
    target_start = line.index('[') + 1
    target_end = line.index(']')
    target = line[target_start:target_end]
    target_state = tuple(1 if c == '#' else 0 for c in target)

    buttons = []
    i = target_end + 1
    while i < len(line):
        if line[i] == '(':
            j = line.index(')', i)
            button_str = line[i + 1:j]
            button = tuple(map(int, button_str.split(',')))
            buttons.append(button)
            i = j + 1
        else:
            i += 1

    return target_state, buttons


def state_after_press(state, button):
    new_state = list(state)
    for light in button:
        new_state[light] = 1 - new_state[light]
    return tuple(new_state)


def min_presses(target_state, buttons):
    n_lights = len(target_state)
    initial_state = tuple([0] * n_lights)

    if initial_state == target_state:
        return 0

    queue = deque([(initial_state, 0)])
    visited = {initial_state}

    while queue:
        state, presses = queue.popleft()

        for button in buttons:
            new_state = state_after_press(state, button)

            if new_state == target_state:
                return presses + 1

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses + 1))

    return -1


if __name__ == '__main__':
    inputs = []
    with open("./input", "r") as file:
        inputs = [line.strip() for line in file.readlines()]

    total_presses = 0
    for line in inputs:
        if line:
            target_state, buttons = parse_line(line)
            min_p = min_presses(target_state, buttons)
            total_presses += min_p

    print(total_presses)
