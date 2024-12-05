import copy
from pprint import pprint

def read_input():
    with open("input.txt", "r") as f:
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
    # pprint(rules)
    updates_to_fix = []
    for update in updates_raw:
        for counter, page in enumerate(update):
            if rules.get(page) and set(rules.get(page)).intersection(set(update[:counter])):
                updates_to_fix.append(update)
                break

    fixed_updates = []
    for update in updates_to_fix:
        new_update = []
        update_len = len(update)
        while len(new_update) < update_len:
            for element in update:
                tmp = copy.deepcopy(update)
                tmp.remove(element)
                if not rules.get(element) or set(rules.get(element)).issuperset(set(tmp)):
                    new_update.append(element)
                    update.remove(element)
        fixed_updates.append(new_update)

    for u in fixed_updates:
        result += int(u[int(len(u) / 2)])
    print(result)