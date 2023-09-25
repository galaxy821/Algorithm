"""
가장 먼 노드 [https://school.programmers.co.kr/tryouts/72093/challenges?language=python3]
"""

from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n+1)]

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    max_dist = 0
    data = []
    visited = [False] * (n+1)

    q = deque()
    q.append((1, 0))
    visited[1] = True

    while q:
        cur, dist = q.popleft()

        if dist == max_dist:
            data.append(cur)
        elif dist > max_dist:
            data.clear()
            data.append(cur)
            max_dist = dist

        for i in graph[cur]:
            if not visited[i]:
                visited[i] = True
                q.append((i, dist+1))

    answer = len(data)
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
