"""
신입사원 교육 [https://school.programmers.co.kr/tryouts/72141/challenges?language=python3]
"""

from heapq import heappush, heappop


def solution(ability, number):
    ability.sort()

    for _ in range(number):
        a = heappop(ability)
        b = heappop(ability)
        temp = a+b
        heappush(ability, temp)
        heappush(ability, temp)


print(solution([10, 3, 7, 2], 2))  # 37
