from pprint import pprint

def read_input():
    with open("input_test.txt", "r") as f:
        data = f.read().splitlines()
    return data

if __name__ == "__main__":
    data = read_input()
    blocks_delimiter = data.index('')
    rules_raw = [v.split("|") for v in data[:blocks_delimiter]]
    updates_raw = [v.split(',') for v in data[blocks_delimiter+1:]]

    rules = dict()
    for v in rules_raw:
        key = v[0]
        value = v[1]
        if rules.get(key):
            rules[key].append(value)
        else:
            rules[key] = [value]

    result = 0
    print(rules)
    for update in updates_raw:
        error = False
        for counter, page in enumerate(update):
            if rules.get(page) and set(rules.get(page)).intersection(set(update[:counter])):
                error = True
                break
        if not error:
            result += int(update[int(len(update)/2)])

    print(result)