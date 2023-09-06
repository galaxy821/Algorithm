"""
3진법 뒤집기
"""

# 문자열을 잘 다루어야하는 문제!!


def solution(n):
    answer = ''

    while n > 0:
        n, re = divmod(n, 3)
        answer += str(re)

    return int(answer, 3)


print(solution(125))
