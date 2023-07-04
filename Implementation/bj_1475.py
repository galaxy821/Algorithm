"""
방 번호 [https://www.acmicpc.net/problem/1475]
"""

n = list(map(int, input()))

count = [0] * 10

for i in n:
    if i == 6 or i == 9:
        if count[6] >= count[9]:
            count[9] += 1
        else:
            count[6] += 1
    else:
        count[i] += 1

print(max(count))
