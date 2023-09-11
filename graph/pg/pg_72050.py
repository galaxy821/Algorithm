"""
거리두기 확인하기 [https://school.programmers.co.kr/tryouts/72050/challenges?language=python3#fn1]
"""

# 각 강의실마다 학생이 있으먄 해당 자리에서 BFS 탐색을 한다.
# 거리 2이내까지만 탐색을 하고 해당 거리 내에 책상이 있으면 계속해서 탐색하고, 파티션이 있으면 해당 탐색에서는 더 탐색하지 않는다.
# 그리고 탐색 도중 거리 2 이내에 학생이 있으면 모든 탐색을 종료하고 False를 반환한다.

from collections import deque

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def search_bfs(place, x, y):
    visited = [[False]*5 for _ in range(5)]
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True

    while q:
        cx, cy, cd = q.popleft()

        for dx, dy in dir:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and cd < 2 and not visited[nx][ny]:
                if place[nx][ny] == "O":
                    visited[nx][ny] = True
                    q.append((nx, ny, cd+1))
                elif place[nx][ny] == "P":
                    return False
    return True


def check_place(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                if not search_bfs(place, i, j):
                    return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(check_place(place))

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
      "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
