"""
나머지 [https://www.acmicpc.net/problem/3052]
"""

values = set()

for _ in range(10) :
    temp = int(input())
    values.add(temp % 42)

print(len(values))