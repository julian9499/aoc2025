

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
        # Read columns right-to-left, each column is a digit
        num_rows = len(problem[0]) - 1  # Last row is operator
        numbers = []
        for col in reversed(problem):
            digits = [col[row] for row in range(num_rows)]
            digit_str = ''.join(digits).strip()
            if digit_str:
                numbers.append(int(digit_str))
        op_row = len(problem[0]) - 1
        op = ''.join(col[op_row] for col in problem).strip()
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