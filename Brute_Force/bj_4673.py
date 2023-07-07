n = [0 for _ in range(10001)]

for i in range(10001):
    temp = i + sum(map(int, str(i)))
    if temp <= 10000:
        n[temp] += 1

for i in range(1, 10001):
    if n[i] == 0:
        print(i)
