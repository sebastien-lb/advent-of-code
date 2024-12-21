

"""
    Read a txt file of the format:
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    and return a list of number for each line
"""
def read_input(file_path: str) -> list:
    with open(file_path, "r") as file:
        lines = file.readlines()
        return [list(map(int, line.strip().split())) for line in lines]
    
def is_report_safe(report):
    if report[0] == report[1]:
        return False
    is_increasing = report[0] < report[1]
    previous = report[0]
    for i in range(1,len(report)):
        if is_increasing and report[i] < previous:
            return False
        if not is_increasing and report[i] > previous:
            return False
        if report[i] == previous:
            return False
        if abs(report[i] - previous) > 3:
            return False
        previous = report[i]    
    return True

def is_report_safe_with_1_pb(report):
    if is_report_safe(report[1:]):
        return True
    is_increasing = report[0] < report[1]
    previous = report[0]
    for i in range(1,len(report)):
        if report[i] == previous:
            return is_report_safe(report[:i] + report[i+1:])
        if is_increasing and report[i] < previous:
            without_i = is_report_safe(report[:i] + report[i+1:])
            without_p = is_report_safe(report[:i-1] + report[i:])
            return without_i or without_p
        if not is_increasing and report[i] > previous:
            without_i = is_report_safe(report[:i] + report[i+1:])
            without_p = is_report_safe(report[:i-1] + report[i:])
            return without_i or without_p
        if abs(report[i] - previous) > 3:
            without_i = is_report_safe(report[:i] + report[i+1:])
            without_p = is_report_safe(report[:i-1] + report[i:])
            return without_i or without_p
        previous = report[i]    
    return True

def main():
    reports = read_input("2024/day_2/input.txt")
    safe_reports = [report for report in reports if is_report_safe(report)]
    print(f"Number of safe reports: {len(safe_reports)}")

    safe_reports_with_1_pb = [report for report in reports if is_report_safe_with_1_pb(report)]
    print(f"Number of safe reports with 1 problem: {len(safe_reports_with_1_pb)}")
main()