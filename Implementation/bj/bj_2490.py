"""
윷놀이 [https://www.acmicpc.net/problem/2490]
"""

for _ in range(3) :
    temp = sum(list(map(int, input().split(" "))))
    if temp == 0 :
        print('D')
    elif temp == 1 :
        print('C')
    elif temp == 2 :
        print('B')
    elif temp == 3 :
        print('A')
    elif temp == 4 :
        print('E')
        
## 다른 풀이
"""
result = ['D', 'C', 'B', 'A', 'E']
for _ in range(3) :
    print(result[sum(list(map(int, input().split(" "))))])
"""