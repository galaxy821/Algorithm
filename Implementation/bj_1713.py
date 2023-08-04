"""
후보 추천하기
"""

n = int(input())
m = int(input())
data = list(map(int, input().split()))

photo = []

for i in range(len(data)):
    isRecom = False
    for j in range(len(photo)):
        if data[i] == photo[j][2]:
            photo[j][0] += 1
            isRecom = True
            break
    if isRecom:
        photo.sort()
        continue
    elif not isRecom and len(photo) < n:
        photo.append([1, i, data[i]])
    elif not isRecom:
        del photo[0]
        photo.append([1, i, data[i]])
    photo.sort()

result = [i[2] for i in photo]
result.sort()
print(*result)
