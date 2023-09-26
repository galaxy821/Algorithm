"""
뒤집기 [acmicpc.net/problem/1439]
"""

n = input()

count0 = 0
count1 = 0

if n[0] == 0:
    count1 += 1
else:
    count0 += 1

for i in range(1, len(n)):
    if n[i-1] != n[i]:
        if n[i] == '1':
            count1 += 1
        else:
            count0 += 1
print(min(count0, count1))

# 다른 풀이
"""
00001100 -> 010
0011001110000 -> 01010
으로 변환해도 동일한 결과를 보여준다.

따라서 순차적으로 숫자가 몇번 바꾸는지 카운트하면 된다.

n = input()

count = 0
for i in range(len(n)-1) :
    if n[i] != n[i+1] :
        count += 1

print((count+1)//2)
"""
