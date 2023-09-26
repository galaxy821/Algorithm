"""
수들의 합 [https://www.acmicpc.net/problem/1789]
"""

n = int(input())

count = 0
sum_value = 0
index = 1
while True:
    if n - sum_value < 2*count+1:
        count += 1
        break
    sum_value += count
    count += 1

print(count)
