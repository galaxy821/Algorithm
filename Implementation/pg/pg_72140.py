"""
실험용 로봇 [https://school.programmers.co.kr/tryouts/72140/challenges?language=python3]
"""

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(command):
    cur_d = 0
    x, y = 0, 0

    for i in command:
        if i == 'L':
            cur_d = cur_d - 1 if cur_d > 0 else 3
        elif i == 'R':
            cur_d = cur_d + 1 if cur_d < 3 else 0
        elif i == 'G':
            x, y = x + d[cur_d][0], y + d[cur_d][1]
        elif i == 'B':
            x, y = x - d[cur_d][0], y - d[cur_d][1]

    return [x, y]


print(solution("GRGLGRG"))  # [2, 2]
