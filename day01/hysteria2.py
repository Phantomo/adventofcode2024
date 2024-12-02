def read_input():
    with open("input.txt", "r") as f:
        data = f.readlines()
    return data

def calculate(data):
    result = 0
    left = []
    right = []
    for line in data:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    for value in left:
        intermid_res = 0
        for appear in right:
            if value == appear:
                intermid_res += value
        result += intermid_res
    return result


if __name__ == "__main__":
    data = read_input()
    print(calculate(data))

