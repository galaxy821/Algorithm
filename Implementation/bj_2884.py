"""
알람시계 [https://www.acmicpc.net/problem/2884]
"""

h, m = map(int, input().split())
if m - 45 >= 0 :
    print(h, m-45)
else :
    if h == 0 :
        print(23, m+15)
    else :
        print(h-1, m+15)
    