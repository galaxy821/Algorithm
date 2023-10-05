"""
조이스틱 [https://school.programmers.co.kr/tryouts/72121/challenges?language=python3]
"""

# a b c d e f g h i j k l m // n o p q r s t u v w x y z


def solution(name):
    answer = 0
    count = len(name) - 1

    if count == 0:
        return (ord(name[count])-ord('A'))

    for i, c in enumerate(name):
        answer += min(ord(c)-ord('A'), ord('Z')-ord(c)+1)

        idx = i + 1

        while idx < len(name) and name[idx] == 'A':
            idx += 1

        count = min(count, 2*i + len(name)-idx, i + 2*(len(name)-idx))

    answer += count

    return answer


print(solution("JEROEN"))  # 56
