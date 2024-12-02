def is_safe(levels):
    increasing = all(1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))
    return increasing or decreasing

def can_be_safe(levels):
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1:]
        if is_safe(new_levels):
            return True
    return False

def count_safe_reports(file):
    with open(file, 'r') as f:
        reports = f.readlines()
    safe_count = 0
    for report in reports:
        levels = list(map(int, report.strip().split()))
        if is_safe(levels) or can_be_safe(levels):
            safe_count += 1
    return safe_count

file = 'day2\input.txt'
print(count_safe_reports(file))