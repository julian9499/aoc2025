

if __name__ == '__main__':

    inputs = []
    with open("./input", "r") as file:
        inputs = [line.rstrip('\n') for line in file.readlines()]

    columns = list(zip(*inputs))
    problems = []
    current_problem = []
    for col in columns:
        if all(c == ' ' for c in col):
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            current_problem.append(col)
    if current_problem:
        problems.append(current_problem)

    results = []
    for problem in problems:
        numbers = []
        for row in range(len(problem[0]) - 1):
            num_str = ''.join(problem[col][row] for col in range(len(problem))).strip()
            if num_str:
                numbers.append(int(num_str))
        op_row = len(problem[0]) - 1
        op = ''.join(problem[col][op_row] for col in range(len(problem))).strip()
        if op == '*':
            result = 1
            for n in numbers:
                result *= n
        elif op == '+':
            result = sum(numbers)
        else:
            continue
        results.append(result)

    print(sum(results))