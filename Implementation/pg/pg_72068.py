"""
카펫 [https://school.programmers.co.kr/tryouts/zk/challenges]
"""

import math


def solution(brown, yellow):
    total = brown + yellow
    answer = []

    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            yw = yellow / i

            if (i+2)*(yw+2) == total:
                answer = [max(yw, i)+2, min(yw, i)+2]
                break
    return answer


print(solution(10, 2))
