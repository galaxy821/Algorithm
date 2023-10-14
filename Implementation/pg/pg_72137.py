"""
체육 대회 [https://school.programmers.co.kr/tryouts/72137/challenges?language=python3]
"""

from itertools import permutations


def solution(ability):
    answer = 0

    for case in list(permutations(range(len(ability)), len(ability[0]))):
        temp = 0
        count = 0
        for i in case:
            temp += ability[i][count]
            count += 1

        answer = max(answer, temp)

    return answer


print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30],
      [70, 0, 70], [100, 100, 100]]))  # 210
