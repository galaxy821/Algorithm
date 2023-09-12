"""
징검다리 건너기 [https://school.programmers.co.kr/tryouts/72079/challenges?language=python3]
"""


def solution(stones, k):
    start, end = min(stones), max(stones)

    answer = 0

    while start <= end:
        mid = (start + end) // 2

        n = 0
        for stone in stones:
            if stone - mid >= 0:
                n = 0
            else:
                n += 1

            if n >= k:
                break

        if n >= k:
            end = mid - 1

        else:
            answer = max(answer, mid)
            start = mid + 1

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
