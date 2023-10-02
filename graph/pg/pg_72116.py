"""
네트워크 [https://school.programmers.co.kr/tryouts/72116/challenges]
"""

from collections import deque


def solution(n, computers):
    answer = 0
    visited = []

    for i in range(n):
        if i not in visited:
            q = deque()
            q.append(i)
            visited.append(i)

            while q:
                cur = q.popleft()

                for j in range(n):
                    if i != j and computers[cur][j] == 1 and j not in visited:
                        q.append(j)
                        visited.append(j)
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
