"""
양과 늑대 [https://school.programmers.co.kr/tryouts/72133/challenges?language=python3]
"""


def solution(info, edges):
    answer = []

    visited = [False] * len(info)

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[c] = False

    visited[0] = True
    dfs(1, 0)

    return max(answer)


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [
      0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))  # 5
