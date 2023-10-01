"""
여행 경로 [https://school.programmers.co.kr/tryouts/72115/challenges?language=python3]
"""

from collections import deque


def solution(tickets):
    answer = []
    n = len(tickets)
    q = deque()
    q.append(("ICN", ["ICN"], []))

    while q:
        cur, path, used = q.popleft()

        if len(used) == n:
            answer.append(path)

        for idx, ticket in enumerate(tickets):
            if ticket[0] == cur and not idx in used:
                q.append((ticket[1], path+[ticket[1]], used+[idx]))

    answer.sort()
    return answer[0]


# ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
