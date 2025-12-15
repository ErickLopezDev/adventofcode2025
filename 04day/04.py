PATH_FILE="04_example.txt"

def can_be_acc( i, j, grid ):
    grid[i-1][j-1]
    grid[i-1][j]
    grid[i-1][i+1]

    grid[i][j-1]
    grid[i][j]
    grid[i][i+1]

    grid[i+1][j-1]
    grid[i+1][j]
    grid[i+1][i+1]
    pass

def printing_department(path_file):
    try:
        grid = []
        total_accesssible = 0
        with open(path_file, 'r') as file:
            lines = file.readlines()
            grid = [list(line.strip()) for line in lines]
            for i in range(len(grid)):
                line = grid[i]
                for j in range(len(line)):
                    # i--:
                    # i: j-- j j++
                    # i++:
                    can_be_acc( i, j, grid )
                    # if can_be_access(i,j):
                        # total_accesssible += 1
                    pass

    except FileNotFoundError:
        print(f"Error: {path_file}")


printing_department(PATH_FILE)
