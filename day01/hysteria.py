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
    left = sorted(left)
    right = sorted(right)
    for i in range(len(left)):
        result += abs(left[i] - right[i])
    return result


if __name__ == "__main__":
    data = read_input()
    print(calculate(data))

