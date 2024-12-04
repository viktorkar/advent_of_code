def get_data(filename):
    with open(filename) as f:
        # Use list comprehension to directly parse data
        return [[int(val) for val in line.split()] for line in f]

def is_report_safe(report):
    is_increasing = report[0] < report[1]

    # Check each pair of adjacent elements
    for current_level, next_level in zip(report, report[1:]):
        difference = abs(current_level - next_level)

        # Validate conditions for "safe"
        if (
            (is_increasing and current_level > next_level)
            or (not is_increasing and current_level < next_level)
            or not (1 <= difference <= 3)
        ):
            return False

    return True


def solve_p1():
    reports = get_data("input.txt")
    safe_count = 0

    for report in reports:
        if is_report_safe(report):
            safe_count += 1

    return safe_count


def solve_p2():
    reports = get_data("input.txt")
    safe_count = 0

    for report in reports:
        if is_report_safe(report):
            safe_count += 1
        else:
            for i in range(len(report)):
                clone = report.copy()
                del clone[i]

                if is_report_safe(clone):
                    safe_count += 1
                    break

    return safe_count


if __name__ == "__main__":
    print("Answer part 1: {}".format(solve_p1()))
    print("Answer part 2: {}".format(solve_p2()))
