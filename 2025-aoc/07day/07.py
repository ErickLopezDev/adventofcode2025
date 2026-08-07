def parse_data(path_file):
    try:
        with open(path_file, "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        print(f"[error] {path_file} not found")
        return None

def check_splits(cols, line):
    new_cols = set()
    counter = 0
    line_len = len(line)
    display_line = list(line)

    for col in cols:
        if line[col] == "^":
            counter += 1
            if col - 1 >= 0:
                new_cols.add(col - 1)
                display_line[col - 1] = "|"
            if col + 1 < line_len:
                new_cols.add(col + 1)
                display_line[col + 1] = "|"
        else:
            new_cols.add(col)
            display_line[col] = "|"

    print("".join(display_line))
    return new_cols, counter

def init_simulation(matrix):
    current_cols = {matrix[0].index("S")}
    total_splits = 0
    for line in matrix:
        current_cols, counter = check_splits(current_cols, line)
        total_splits += counter
    print(f"\nTotal splits: {total_splits}")
    return total_splits

FILE_PATH = "07.txt"
matrix = parse_data(FILE_PATH)
init_simulation(matrix)
