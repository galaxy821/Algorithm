"""
기능 개발 [https://school.programmers.co.kr/tryouts/72092/challenges?language=python3]
"""

from collections import deque
import math


def solution(progresses, speeds):
    left_day = [math.ceil((100-progresses[i])/speeds[i])
                for i in range(len(progresses))]
    answer = []

    q = deque(left_day)

    while q:
        cur = q.popleft()

        n = 1

        while q and cur >= q[0]:
            q.popleft()
            n += 1

        answer.append(n)

    return answer


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]
