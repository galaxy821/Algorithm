"""
외톨이 알파벳 [https://school.programmers.co.kr/tryouts/72136/challenges?language=python3]
"""


def solution(input_string):
    answer = ''

    dic = {input_string[0]: 1}

    for i in range(1, len(input_string)):
        if input_string[i-1] != input_string[i]:
            dic[input_string[i]] = dic.get(input_string[i], 0) + 1

    for key, value in dic.items():
        if value >= 2:
            answer += key

    if len(answer) == 0:
        return 'N'
    else:
        return ''.join(sorted(list(answer)))


solution("edeaaabbccd")  # "de"
