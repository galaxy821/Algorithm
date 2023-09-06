"""
교점에 별 만들기
"""

from itertools import combinations


def find_intersection_point(line1, line2):
    a, b, c = line1
    d, e, f = line2

    if b*d == e*a:
        return None

    x = (b*f-c*e)/(a*e-b*d)
    y = (a*f-c*d)/(b*d-a*e)

    if x == int(x) and y == int(y):
        return (int(x), int(y))
    else:
        return None


def solution(line):
    n = len(line)

    comb_lines = list(combinations(line, 2))
    points = set()

    for line1, line2 in comb_lines:
        point = find_intersection_point(line1, line2)

        if point:
            points.add(point)

    x_points = [point[0] for point in points]
    x_min = min(x_points)
    x_max = max(x_points)

    y_points = [point[1] for point in points]
    y_min = min(y_points)
    y_max = max(y_points)

    board = ['.' * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]

    for x, y in points:
        board[y_max-y] = board[y_max-y][:x - x_min] + \
            '*'+board[y_max-y][x-x_min+1:]

    return board


print(solution([[2, -1, 4], [-2, -1, 4],
      [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
