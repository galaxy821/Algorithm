"""
소수 찾기 [https://school.programmers.co.kr/tryouts/72069/challenges]
"""

from itertools import permutations
import math


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    list_digit = list(numbers)
    answer = 0
    set_num = set()

    for i in range(1, len(numbers)+1):
        for number in list(permutations(list_digit, i)):
            temp = int(''.join(number))
            if temp not in set_num and is_prime(temp):
                set_num.add(temp)
                answer += 1

    return answer


print(solution("011"))
