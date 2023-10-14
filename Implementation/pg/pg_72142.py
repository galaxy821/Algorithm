"""
카페 확장 [https://school.programmers.co.kr/tryouts/72142/challenges?language=python3]
"""

from collections import deque


def solution(menu, order, k):
    queue = deque()
    busy = -1
    answer = 0
    idx = 0

    for t in range(k * (len(order)-1)+1):
        if k * idx == t:
            queue.append(order[idx])
            idx += 1

        if busy == t:
            queue.popleft()
            busy = -1

        if busy == -1 and len(queue) > 0:
            busy = t + menu[queue[0]]

        answer = max(answer, len(queue))

    return answer


print(solution([5, 12, 30], [1, 2, 0, 1], 10))  # 3
