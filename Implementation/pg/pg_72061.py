"""
핸드폰 번호 가리기 [https://school.programmers.co.kr/tryouts/72061/challenges?language=python3]
"""


def solution(phone_number):
    answer = '*'*(len(phone_number)-4) + phone_number[-4:]
    return answer


print(solution("01012341234"))
