file_path = '01.txt'
min_value = 0
max_value = 99
def decode_rotations(initial_position):
    counter = initial_position
    output = 0 
    try: 
        with open(file_path, 'r') as file:
            for line in file:
                direction = line[0]
                steps = int(line[1:])
                if direction == 'L':
                    counter -= steps
                    if counter < min_value:
                        counter = (counter % (max_value + 1) + (max_value + 1)) % (max_value + 1)
                        output += 1
                if direction == 'R':
                    counter += steps
                    if counter > max_value:
                        counter = counter % (max_value + 1)
                        output += 1
            print(output)
    except FileNotFoundError:
        print(f"Error: file {file_path} was not found.")

decode_rotations(50)

