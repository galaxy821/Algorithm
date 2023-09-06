"""
이진 변환 반복하기 [https://school.programmers.co.kr/tryouts/72058/challenges?language=python3]
"""


def solution(s):
    temp = s

    count_cycle = 0
    count_rm_zero = 0

    while len(temp) > 1:
        print("before", temp)
        count_rm_zero += temp.count('0')
        count_cycle += 1
        temp = temp.replace('0', "")
        print("after", temp)
        temp = str(bin(int(len(temp))))[2:]

    answer = [count_cycle, count_rm_zero]

    return answer


print(solution("110010101001"))
