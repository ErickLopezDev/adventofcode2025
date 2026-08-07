file_path = '09.txt'

def main():
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        points = [tuple(map(int, line.split(','))) for line in data.strip().splitlines()]
        max_area = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dx = abs(x1 - x2)
                dy = abs(y1 - y2)
                area = (dx + 1) * (dy + 1)
                if area > max_area:
                    max_area = area
        print(max_area)
    except FileNotFoundError:
        print(f"Error: file {file_path} was not found.")

main()
