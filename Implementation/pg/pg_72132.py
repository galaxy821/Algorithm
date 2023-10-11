"""
양궁대회 [https://school.programmers.co.kr/tryouts/72132/challenges]
"""

from itertools import combinations_with_replacement


def solution(n, info):
    answer = [-1]
    max_gap = 0

    for case in list(combinations_with_replacement(range(11), n)):
        info2 = [0] * 11

        for i in case:
            info2[10-i] += 1

        appeach, ryan = 0, 0
        for i in range(11):
            if info[i] == info2[i] and info[i] == 0:
                continue
            elif info[i] >= info2[i]:
                appeach += (10 - i)
            else:
                ryan += (10 - i)

        if ryan > appeach:
            gap = ryan - appeach

            if gap > max_gap:
                max_gap = gap
                answer = info2

    return answer


# [0,2,2,0,1,0,0,0,0,0,0]
print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
