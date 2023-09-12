"""
징검다리 [https://school.programmers.co.kr/tryouts/72078/challenges]
"""


def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    start, end = 1, distance
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        rm_rock = 0
        pre_rock = 0

        for rock in rocks:
            if rock - pre_rock < mid:
                rm_rock += 1
            else:
                pre_rock = rock

            if rm_rock > n:
                break

        if rm_rock > n:
            end = mid - 1
        else:
            answer = mid
            start = mid+1

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
