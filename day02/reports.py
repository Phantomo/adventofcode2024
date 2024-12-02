def read_input():
    with open("input_test.txt", "r") as f:
        data = f.readlines()
    return data


def is_safe_report(report: list[int]) -> bool:
    is_report_asc = True
    if report[0] > report[1]:
        is_report_asc = False

    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        if diff < 1 or diff > 3:
            return False
        if report[i] < report[i - 1] and is_report_asc:
            return False
        if report[i] > report[i - 1] and not is_report_asc:
            return False
    return True


if __name__ == "__main__":
    data = read_input()
    safe_reports = 0
    for line in data:
        report = [int(v) for v in line.split()]
        # print(report)
        if is_safe_report(report):
            # print("Safe report")
            safe_reports += 1
    print(safe_reports)