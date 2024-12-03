import re

def read_input():
    with open("input.txt", "r") as f:
        data = f.read()
    return data

def multiple_count(data):
    result = 0
    groups = re.findall(r"(do\(\))|(mul\(([0-9][0-9]*[0-9]*,[0-9][0-9]*[0-9]*)\))|(don't\(\))", data)
    active = True
    for group in groups:
        if group[0]:
            active = True
        if group[3]:
            active = False
        if group[2] and active:
            a,b = group[2].split(",")
            result += int(a) * int(b)
    return result

if __name__ == "__main__":
    data = read_input()
    print(multiple_count(data))