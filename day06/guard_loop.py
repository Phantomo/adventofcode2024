import copy


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
    routes = dict()
    def _add_new_route(x, y, direction):
        if routes.get((x, y)):
            routes[(x, y)].add(direction)
        else:
            routes[(x, y)] = {direction}

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
        _add_new_route(pos_x, pos_y, direction)
        new_pos_x = pos_x + direction[0]
        new_pos_y = pos_y + direction[1]
    return data, routes


def find_loop_route(data, pos_x, pos_y, direction):
    column_length = len(data)
    row_length = len(data[0])
    new_pos_x = pos_x
    new_pos_y = pos_y
    obstacles = set()

    same_obstacles = 0
    while 0 <= new_pos_x < column_length and 0 <= new_pos_y < row_length:
        if data[new_pos_x][new_pos_y] == "#":
            direction = update_direction_90_deg(direction)
            if (new_pos_x, new_pos_y) in obstacles:
                same_obstacles += 1
                if same_obstacles == 4:
                    return True
            else:
                same_obstacles = 0
                obstacles.add((new_pos_x, new_pos_y))
        else:
            pos_x = new_pos_x
            pos_y = new_pos_y

        new_pos_x = pos_x + direction[0]
        new_pos_y = pos_y + direction[1]
    return False


if __name__ == "__main__":
    data = read_input()
    direction = None
    initial_position = None

    data = [list(row) for row in data]

    for x, row in enumerate(data):
        for y, cell in enumerate(row):
            match cell:
                case "^":
                    direction = (-1, 0)
                    initial_position = (x, y)
                    data[x][y] = "."
                case  "v":
                    direction = (1, 0)
                    initial_position = (x, y)
                    data[x][y] = "."
                case ">":
                    direction = (0, 1)
                    initial_position = (x, y)
                    data[x][y] = "."
                case "<":
                    direction = (0, -1)
                    initial_position = (x, y)
                    data[x][y] = "."

    new_map, routes = calculate_guard_route(data, initial_position[0], initial_position[1], direction)

    result = 0
    for point in routes.keys():
        new_data = copy.deepcopy(data)
        new_data[point[0]][point[1]] = "#"
        if find_loop_route(new_data, initial_position[0], initial_position[1], direction):
            result += 1

    # for line in new_map:
    #     print(line)
    #
    # print(routes)
    print(result)