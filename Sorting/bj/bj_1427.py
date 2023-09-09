"""
소트인사이드 [https://www.acmicpc.net/problem/1427]
"""

value = list(map(int, input()))
value = sorted(value, reverse=True)

print("".join(map(str, value)))
