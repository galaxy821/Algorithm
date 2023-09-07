"""
문자열 다루기 [https://school.programmers.co.kr/tryouts/72060/challenges?language=python3]
"""


def solution(s):
    length = len(s)
    if (length == 4 or length == 6) and s.isdigit() == True:
        return True
    else:
        return False


print(solution("1234"))
