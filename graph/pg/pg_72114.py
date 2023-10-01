"""
타깃 넘버 [https://school.programmers.co.kr/tryouts/72114/challenges?language=python3]
"""

from collections import deque


def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = deque()
    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))

    while q:
        temp, idx = q.popleft()
        idx += 1

        if idx < n:
            q.append((temp + numbers[idx], idx))
            q.append((temp - numbers[idx], idx))
        else:
            if temp == target:
                answer += 1

    return answer


print(solution([1, 1, 1, 1, 1], 3))  # 5
