file_path = '01.txt'
min_value = 0
max_value = 100

def decode_rotations(initial_position):
    dial = initial_position
    accu = 0 
    try: 
        with open(file_path, 'r') as file:
            for line in file:
                print(dial)
                line = line.strip()
                print(line)

                direction = line[0]
                steps = int(line[1:])

                if direction == 'L':
                    for _ in range(steps):
                        dial -= 1
                        if dial == min_value:
                            print('RCH 0')
                            accu += 1
                        if dial < min_value:
                            dial += max_value

                if direction == 'R':
                    for _ in range(steps):
                        dial += 1
                        if dial >= max_value:
                            dial -= max_value
                        if dial == min_value:
                            print('RCH0')
                            accu += 1

            print(f"result total times: {accu}")

    except FileNotFoundError:
        print(f"Error: file {file_path} was not found.")

decode_rotations(50)
