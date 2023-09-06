"""
짝지어 제거하기 [https://school.programmers.co.kr/tryouts/72055/challenges?language=python3]
"""

# 스텍을 활용하는 문제
# 일단 스텍에 추가하다가 스텍의 최상단의 문자와 같은 문자가 발견되면 스택 최상단 원소를 pop한다.
# 최종적으로 스텍이 비어 있으면 짝지어 제거하기에 성공. 스택이 비어 있지 않으면 실패한 것으로 간주


def solution(s):
    stack = []

    for i in s:
        if len(stack) > 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        return 1
    else:
        return 0


print(solution("baabaa"))
