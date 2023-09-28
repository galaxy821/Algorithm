"""
줄 서는 방법 [https://school.programmers.co.kr/tryouts/72113/challenges?language=python3]
"""

import math


def solution(n, k):
    answer = [i for i in range(1, n+1)]
    stack = []
    k -= 1

    while n > 0:
        a = k // math.factorial(n-1)
        stack.append(answer[a])
        del answer[a]

        k = k % math.factorial(n - 1)
        n -= 1

    return stack


print(solution(3, 5))  # [3,1,2]
