def read_input():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    return data


def find(line: str, start_pos: int, word: str):
    # print(line)
    # print(start_pos)
    result = 0
    word_len = len(word)
    if len(line) >= word_len + start_pos:
        if line[start_pos: word_len + start_pos] == word:
            result += 1
    if start_pos + 1 - word_len >= 0: # check reversed
        if line[start_pos - word_len + 1: start_pos + 1] == word[::-1]:
            result += 1
    return result


def find_diagonal(data, pos_x: int, pos_y: int, word: str):
    result = 0
    row_len = len(data)
    column_len = len(data[0])
    word_len = len(word)

    diagonals = []
    if pos_x + 1 - word_len >= 0 and pos_y + 1 - word_len >= 0:
         diagonals.append("".join(data[pos_x - counter][pos_y - counter] for counter in range(word_len)))

    if pos_x + word_len <= row_len and pos_y + word_len <= column_len:
        diagonals.append("".join(data[pos_x+counter][pos_y+counter] for counter in range(word_len)))

    if pos_x + 1 - word_len >= 0 and pos_y + word_len <= column_len:
        diagonals.append("".join(data[pos_x - counter][pos_y+counter] for counter in range(word_len)))

    if pos_x + word_len <= row_len and pos_y + 1 - word_len >= 0:
        diagonals.append("".join(data[pos_x+counter][pos_y - counter] for counter in range(word_len)))

    # print("Diagonals", diagonals)
    for d in diagonals:
        if d in (word, word[::-1]):
            result += 1
    return result

def super_search(data, word: str = "XMAS"):
    result = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == word[0]:
                result += find(data[x], y, word) # find for horizontal line
                result += find("".join(data[tmp_x][y] for tmp_x in range(len(data))), x, word) # find for vertical line
                result += find_diagonal(data, x, y, word)
                # print(result)

    return result

if __name__ == "__main__":
    data = read_input()
    print(super_search(data))