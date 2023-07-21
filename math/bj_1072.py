"""
게임 [https://www.acmicpc.net/problem/1072]
"""

x, y = map(int, input().split(" "))

start = 1
end = int(1e9)

result = -1
rate = (y*100) // x

if rate > 99:
    print(-1)
else:
    while start <= end:
        mid = start + (end - start) // 2

        if (mid+y) * 100 // (mid+x) > rate:
            result = mid
            end = mid - 1
        else:
            start = mid+1
    print(result)
