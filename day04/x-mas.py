def read_input():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    return data


def super_search(data, word: str = "MAS"):
    result = 0
    word_len = len(word)
    row_len = len(data)
    column_len = len(data[0])

    for x in range(len(data)):
        for y in range(len(data[x])):
            diagonals = []
            if data[x][y] == "A":
                top_left_pos_x = x-1
                top_left_pos_y = y-1
                if top_left_pos_x >= 0 and top_left_pos_y >= 0:
                    if top_left_pos_x + word_len <= row_len and top_left_pos_y + word_len <= column_len:
                        diagonals.append("".join(data[top_left_pos_x + counter][top_left_pos_y + counter] for counter in range(word_len)))
                bottom_left_pos_x = x+1
                bottom_left_pos_y = y-1
                if bottom_left_pos_x < row_len and bottom_left_pos_y >= 0:
                    if bottom_left_pos_x + 1 - word_len >= 0 and bottom_left_pos_y + word_len <= column_len:
                        diagonals.append("".join(data[bottom_left_pos_x - counter][bottom_left_pos_y + counter] for counter in range(word_len)))
            intermid_res = 0
            for d in diagonals:
                if d in (word, word[::-1]):
                    intermid_res += 1
            if intermid_res == 2:
                result += 1

    return result

if __name__ == "__main__":
    data = read_input()
    print(super_search(data))