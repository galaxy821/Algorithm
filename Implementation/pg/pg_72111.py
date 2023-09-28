"""
2개 이하로 다른 비트 [https://school.programmers.co.kr/tryouts/72111/challenges?language=python3]
"""


def cal_min_value(number):
    if number % 2 == 0:
        return number + 1

    y = '0' + bin(number)[2:]
    idx = y.rfind('0')
    y = list(y)
    y[idx] = '1'
    y[idx+1] = '0'

    return int(''.join(y), 2)


def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(cal_min_value(num))

    return answer


print(solution([2, 7]))
