"""
나머지와 몫이 같은 수 [https://www.acmicpc.net/problem/1834]
"""

n = int(input())

tot = 0
idx = 1

while True:
    if ((n+1)*idx) // n >= n:
        print(tot)
        break
    else:
        tot += ((n+1)*idx)
    idx += 1
