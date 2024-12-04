from enum import Enum

"""
input is a series of reports with one report per line. each report is a series
of numbers separated by spaces called levels.

find which reports are safe. A report only counts as safe if both of the
following are true:
- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.
"""

reports = []
with open("2/input.txt", "r") as file:

    for line in file:
        levels = line.strip().split(" ")
        levels = list(map(lambda string: int(string), levels))
        reports.append(levels)

print(reports[0:4])

reports = [
    [7, 6, 4, 2, 1][1, 2, 7, 8, 9][9, 7, 6, 2, 1][1, 3, 2, 4, 5][8, 6, 4, 4, 1][
        1, 3, 6, 7, 9
    ]
]

safeTotal = 0
for report in reports:

    if report[0] == report[1]:
        continue

    isRising = report[0] < report[1]

    safe = True
    for i in range(0, len(report) - 1):
        if report[i] < report[i + 1] != isRising:
            safe = False
            break

        if abs(report[i] - report[i + 1] > 3):
            safe = False
            break

    if safe == True:  # meaning it passed both tests
        safeTotal += 1

print(f"total: {safeTotal}")
