"""
주식가격 [https://school.programmers.co.kr/tryouts/72091/challenges?language=python3]
"""


from collections import deque


def solution(prices):  # stack
    answer = [i for i in range(len(prices)-1, -1, -1)]

    stack = [0]

    for i in range(1, len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j

        stack.append(i)

    return answer


def solution2(prices):  # queue
    answer = []
    q = deque(prices)

    while q:
        price = q.popleft()
        sec = 0
        for i in q:
            sec += 1
            if price > i:
                break
        answer.append(sec)
    return answer


print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
print(solution2([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
