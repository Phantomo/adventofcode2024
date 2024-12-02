def read_input():
    with open("input.txt", "r") as f:
        data = f.readlines()
    return data

def is_asc_order(first_value, second_value):
    is_report_asc = True
    if first_value > second_value:
        is_report_asc = False
    return is_report_asc

def is_safe_report(report: list[int], error_threshold=1) -> bool:
    def _check_updated(report: list[int]) -> bool:
        if is_safe_report(report[:i] + report[i + 1:], 0) or is_safe_report(report[:i - 1] + report[i:], 0):
            return True
        if i - 2 >= 0 and is_safe_report(report[:i-2] + report[i-1:], 0): # цього спершу не було
            return True
        return False

    is_report_asc = is_asc_order(report[0], report[1])
    i = 1
    while i < len(report):
        diff = abs(report[i] - report[i - 1])
        if (diff < 1 or diff > 3) or (report[i] < report[i - 1] and is_report_asc) or (report[i] > report[i - 1] and not is_report_asc):
            if error_threshold:
                return _check_updated(report)
            return False
        i += 1
    return True


if __name__ == "__main__":
    data = read_input()
    safe_reports = 0
    for line in data:
        report = [int(v) for v in line.split()]
        if is_safe_report(report):
            safe_reports += 1
        else:
    print(safe_reports)