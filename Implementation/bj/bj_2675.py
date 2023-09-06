"""
문자열 반복 [https://www.acmicpc.net/problem/2675]
"""

n = int(input())
for _ in range(n) :
    i, value = input().split()
    temp = list()
    for j in value :
        for _ in range(int(i)) :
            temp.append(j)
    print(''.join(temp))