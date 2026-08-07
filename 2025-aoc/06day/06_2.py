import math

def parse_data(path_file): 
    matrix_data = []
    operators = []
    try:
        with open(path_file, "r") as f:
            all_lines = [row.rstrip('\n') for row in f.readlines()]
            if not all_lines: return None, None
            max_w = max(len(l) for l in all_lines)
            padded = [l.ljust(max_w) for l in all_lines]
            operator_line = padded[-1]
            matrix_lines = padded[:-1]

            cols = [list(c) for c in zip(*matrix_lines)]
            current_problem_numbers = []
            for i in range(len(cols) - 1, -1, -1):
                col_chars = cols[i]
                val_str = "".join(col_chars).strip()
                if val_str:
                    current_problem_numbers.append(int(val_str))
                if not val_str or i == 0:
                    if current_problem_numbers:
                        op = '+'
                        for j in range(i, i + len(current_problem_numbers) + 1):
                            if j < len(operator_line) and operator_line[j] in '+*':
                                op = operator_line[j]
                                break
                        matrix_data.append(current_problem_numbers)
                        operators.append(op)
                        current_problem_numbers = []
    except Exception as e:
        print(f"[error]: {e}")
        return None, None
    return matrix_data, operators

def operate_sign(cols, operators):
    results = {}
    for i, col in enumerate(cols):
        sign = operators[i]
        col_name = f"col: {i}_{sign}"
        if sign == '+':
            results[col_name] = sum(col)
        elif sign == '*':
            results[col_name] = math.prod(col)
        else:
            results[col_name] = 0
    final_sum = 0
    for value in results.values():
        if isinstance(value, (int, float)):
            final_sum += value
    return results, final_sum

PATH_FILE = "06.txt"

columns, operators = parse_data(PATH_FILE)
result, _sum = operate_sign(columns, operators)

print(_sum)
