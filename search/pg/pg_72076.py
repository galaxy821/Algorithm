"""
입국심사 [https://school.programmers.co.kr/tryouts/72076/challenges?language=python3]
"""


def solution(n, times):
    start, end = 1, n*max(times)
    answer = 0

    while start <= end:
        mid = start + (end-start)//2

        count = 0
        for time in times:
            count += mid // time

            if count >= n:
                break

        if count >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


print(solution(6, [7, 10]))
