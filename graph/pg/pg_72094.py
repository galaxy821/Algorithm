"""
순위 [https://school.programmers.co.kr/tryouts/72094/challenges?language=python3]
"""

INF = int(1e9)


def solution(n, results):
    graph = [[INF]*(n+1) for _ in range(n+1)]

    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0

    for a, b in results:
        graph[a][b] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    answer = 0

    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if graph[i][j] != INF or graph[j][i] != INF:
                count += 1

        if count == n:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))  # 2
