"""
단어 변환 [https://school.programmers.co.kr/tryouts/72118/challenges?language=python3]
"""

from collections import deque


def solution(begin, target, words):
    answer = 0

    n = len(begin)
    q = deque()
    visited = [False] * len(words)

    q.append((begin, 0))

    while q:
        cur, depth = q.popleft()

        if cur == target:
            answer = depth

        for i in range(len(words)):
            if not visited[i]:
                count = 0
                for j in range(n):
                    if cur[j] != words[i][j]:
                        count += 1

                if count == 1:
                    q.append((words[i], depth+1))
                    visited[i] = True

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
