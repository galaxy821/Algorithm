"""
큰 수 만들기 [https://school.programmers.co.kr/tryouts/72122/challenges?language=python3]
"""


def solution(number, k):

    stack = []

    for i in number:
        while k > 0 and stack and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)

    return "".join(stack[:len(number)-k])


print(solution("4177252841", 4))  # "775841"
