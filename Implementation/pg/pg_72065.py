"""
호텔 방 배정 [https://school.programmers.co.kr/tryouts/72065/challenges?language=python3]
"""

# 효율성 테스트 실해
import sys


def solution(k, room_number):
    result = set()
    answer = list()

    for number in room_number:
        if number not in result:
            result.add(number)
            answer.append(number)
        else:
            for i in range(number+1, k):
                if i not in result:
                    result.add(i)
                    answer.append(i)
                    break
    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))

# 효율성 테스트 성공

sys.setrecursionlimit(10000000)


def find_room(n, room):
    if n not in room:
        room[n] = n+1
        return n

    result = find_room(room[n], room)
    room[n] = result+1
    return result


def solution2(k, room_number):
    room = dict()
    answer = list()

    for number in room_number:
        answer.append(find_room(number, room))

    return answer


print(solution2(10, [1, 3, 4, 1, 3, 1]))
