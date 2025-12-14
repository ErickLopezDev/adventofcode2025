path_file = '02.txt'

def is_invalid_id(number):
    s = str(number)
    N = len(s)

    for patter_length in range(1, N // 2 + 1):
        # is a divisor of the total length
        if N % patter_length == 0:
            # takes first chunk of possible pattern
            pattern = s[:patter_length]
            # how much times can the pattern repeat
            k = N // patter_length
            # check if possible patter is equals to the input number
            if pattern * k == s:
                return True
    return False


def gift_shop():
    total_invalid_ids = 0
    all_invalid_ids_found = []

    try:
        with open(path_file, 'r') as file:
            arr = file.read().strip()
            ranges = arr.split(',')

            for range_str in ranges:
                current_range_str = range_str.strip()
                parts = current_range_str.split('-')
                if len(parts) != 2:
                    continue
                try:
                    nl = int(parts[0].strip())
                    nr = int(parts[1].strip())

                    for number in range(nl, nr + 1):
                        if is_invalid_id(number):
                            all_invalid_ids_found.append(number)
                            total_invalid_ids += 1
                except ValueError:
                    print(f"Error: non integer error at:'{current_range_str}'")
            print(f"invalid ids: {all_invalid_ids_found}")
            print(f"sum: {sum(all_invalid_ids_found)}")

    except FileNotFoundError:
        print(f"Error: file {path_file} was not found.")

gift_shop()
