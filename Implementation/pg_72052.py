"""
시저 암호 [https://school.programmers.co.kr/tryouts/72052/challenges?language=python3]
"""

# 흔한 아스키 코드 활용하는 문제


def solution(s, n):
    answer = ''
    for i in s:
        if 65 <= ord(i) <= 90:
            if ord(i)+n > 90:
                answer += chr(ord(i)+n - 26)
            else:
                answer += chr(ord(i)+n)
        elif 97 <= ord(i) <= 122:
            if ord(i)+n > 122:
                answer += chr(ord(i)+n - 26)
            else:
                answer += chr(ord(i)+n)
        else:
            answer += i
    return answer
