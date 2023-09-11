"""
가장 큰수 [https://school.programmers.co.kr/tryouts/72075/challenges?language=python3]
"""


def solution(numbers):
    numbers = list(map(str, numbers))
    sorted_nums = sorted(numbers, key=lambda x: x*3, reverse=True)
    answer = ''.join(sorted_nums)
    return str(int(answer))


print(solution([3, 30, 34, 5, 9]))
