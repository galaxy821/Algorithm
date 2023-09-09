"""
두 개 뽑아서 더하기 [https://school.programmers.co.kr/tryouts/72072/challenges?language=python3]
"""

from itertools import permutations


def solution(numbers):
    answer = set()
    for case in list(permutations(numbers, 2)):
        answer.add(case[0]+case[1])

    answer = sorted(answer)
    return answer


print(solution([2, 1, 3, 4, 1]))
