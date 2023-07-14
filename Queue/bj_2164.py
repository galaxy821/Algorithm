"""
카드2 [https://www.acmicpc.net/problem/2164]
"""

from collections import deque

n = int(input())

card_queue = deque([i for i in range(1, n+1)])
last_card = 0

while True:
    last_card = card_queue.popleft()
    if len(card_queue) == 0:
        break
    card_queue.append(card_queue.popleft())

print(last_card)
