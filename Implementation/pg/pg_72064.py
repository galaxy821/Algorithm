"""
모음 사전 [https://school.programmers.co.kr/tryouts/72064/challenges?language=python3]
"""

from itertools import product


def solution(word):
    answer = []

    li = ['A', 'E', 'I', 'O', 'U']

    for i in range(1, 6):
        for j in product(li, repeat=i):
            answer.append(''.join(j))

    answer.sort()
    return answer.index(word)+1


print(solution("AAAAE"))
