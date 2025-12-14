path_file = '02.txt'

def is_invalid_id(number):
    s = str(number)
    n = len(s)

    if n % 2 != 0:
        return False

    # string must to be symetric to be consider a pattern
    half_length = n // 2
    first_half = s[:half_length]
    second_half = s[half_length:]
    return first_half == second_half

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
                
                nl = int(parts[0].strip())
                nr = int(parts[1].strip())

                for number in range(nl, nr + 1):
                    if is_invalid_id(number):
                        all_invalid_ids_found.append(number)
                        total_invalid_ids += 1

            
            print(f"{sum(all_invalid_ids_found)}")

    except FileNotFoundError:
        print(f"Error: file {path_file} was not found")

gift_shop()
