def read_input():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    return data


def update_direction_90_deg(current_direction: tuple[int, int]) -> tuple[int, int]:
    # (-1, 0) -> (0, 1) -> (1, 0) -> (0, -1)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_index = directions.index(current_direction)
    return directions[curr_index+1] if curr_index + 1 < len(directions) else directions[0]


def calculate_guard_route(data, pos_x, pos_y, direction):
    column_length = len(data)
    row_length = len(data[0])
    new_pos_x = pos_x
    new_pos_y = pos_y
    while 0 <= new_pos_x < column_length and 0 <= new_pos_y < row_length:
        if data[new_pos_x][new_pos_y] == "#":
            direction = update_direction_90_deg(direction)
        else:
            data[new_pos_x][new_pos_y] = "X"
            pos_x = new_pos_x
            pos_y = new_pos_y
        new_pos_x = pos_x + direction[0]
        new_pos_y = pos_y + direction[1]
    return data

if __name__ == "__main__":
    data = read_input()
    direction = None
    current_position = None

    data = [list(row) for row in data]

    for x, row in enumerate(data):
        for y, cell in enumerate(row):
            match cell:
                case "^":
                    direction = (-1, 0)
                    current_position = (x, y)
                    data[x][y] = "."
                case  "v":
                    direction = (1, 0)
                    current_position = (x, y)
                    data[x][y] = "."
                case ">":
                    direction = (0, 1)
                    current_position = (x, y)
                    data[x][y] = "."
                case "<":
                    direction = (0, -1)
                    current_position = (x, y)
                    data[x][y] = "."

    new_map = calculate_guard_route(data, current_position[0], current_position[1], direction)

    result = 0
    for row in new_map:
        for cell in row:
            if cell == "X":
                result += 1

    print(result)