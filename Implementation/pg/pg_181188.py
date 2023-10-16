"""
요격 시스템 [https://school.programmers.co.kr/learn/courses/30/lessons/181188]
"""


def solution(targets):
    answer = 0

    targets.sort(key=lambda x: (x[1], x[0]))

    cur = 0

    for i in range(len(targets)):
        if targets[i][0] >= cur:
            cur = targets[i][1]
            answer += 1

    return answer


print(solution([[4, 5], [4, 8], [10, 14], [
      11, 13], [5, 12], [3, 7], [1, 4]]))  # 3
