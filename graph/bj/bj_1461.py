"""
도서관 [https://www.acmicpc.net/problem/1461]
"""

n, k = map(int, input().split())
data = list(map(int, input().split()))

plus = []
minus = []
max_value = 0

for i in data:
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)

    if abs(max_value) < abs(i):
        max_value = i

plus.sort(reverse=True)
minus.sort()

walking = 0

for j in range(0, len(plus), k):
    if plus[j] != max_value:
        walking += plus[j]

for j in range(0, len(minus), k):
    if minus[j] != max_value:
        walking += abs(minus[j])

walking *= 2
walking += abs(max_value)

print(walking)
