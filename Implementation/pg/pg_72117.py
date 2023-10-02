"""
괄호 변환 [https://school.programmers.co.kr/tryouts/72117/challenges?language=python3]
"""

import sys

sys.setrecursionlimit(10**6)


def check_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        elif p[i] == ')':
            count -= 1
        if count == 0:
            return i
    return 0


def check_valid(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        elif p[i] == ')' and count > 0:
            count -= 1
        else:
            return False
    return True


def solution(p):
    answer = ''

    if len(p) == 0:
        return answer

    index = check_index(p)
    u = p[:index+1]
    v = p[index+1:]

    if check_valid(u):
        answer = (u + solution(v))
    else:
        answer = "("+solution(v)+")"

        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += ''.join(u)

    return answer


print(solution("(()())()"))  # "(()())()"
