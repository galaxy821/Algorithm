"""
문열 내 마음대로 정렬하기 [https://school.programmers.co.kr/tryouts/72074/challenges?language=python3]
"""


def solution(strings, n):
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer


print(solution(["sun", "bed", "car"], 1))
