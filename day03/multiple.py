import re

def read_input():
    with open("input.txt", "r") as f:
        data = f.read()
    return data

def multiple_count(data):
    result = 0
    groups = re.findall(r"mul\(([0-9][0-9]*[0-9]*,[0-9][0-9]*[0-9]*)\)", data)
    for operators in groups:
        a,b = operators.split(",")
        result += int(a) * int(b)
    return result

if __name__ == "__main__":
    data = read_input()
    print(multiple_count(data))