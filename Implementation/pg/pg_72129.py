"""
k진수에서 소수 구하기 [https://school.programmers.co.kr/tryouts/72129/challenges?language=python3]
"""

import math


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0

    temp = ""
    while n > 0:
        n, mod = divmod(n, k)
        temp += str(mod)

    converted = temp[::-1]
    print(converted)
    num = ""
    for i in range(len(converted)-1):
        if converted[i] != '0':
            num += converted[i]
            if converted[i+1] == '0':
                print(num)
                if is_prime(int(num)):
                    answer += 1
                num = ""

    if converted[-1] != '0':
        num += converted[-1]

    if len(num) > 0 and is_prime(int(num)):
        print(num)
        answer += 1

    return answer


print(solution(437674, 3))  # 3
