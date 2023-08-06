"""
포도주 시식 [https://www.acmicpc.net/problem/2156]
"""

import sys

n = int(sys.stdin.readline())

data = [int(sys.stdin.readline()) for _ in range(n)]
dp = [[0, 0] for _ in range(n+1)]
dp[1] = [data[0], 0]

for i in range(1, n):
    dp[i+1][0] = max(dp[i-1][0], dp[i-1][1]) + data[i]
    dp[i+1][1] = max(dp[i][0] + data[i], dp[i][1])

print(max(map(max, dp)))


"""
참고하면 좋은 글! [https://www.acmicpc.net/board/view/60664]

dp[n]은 n번째 와인까지 따졌을 때 마실 수 있는 와인의 최대 양이죠?

본인이 직접 설명한 것처럼 현재 코드에서 고려하는 것은

1. 전전(n-2)까지의 최대 양 + 현재 양 = (dp[n-2] + wine[n])
2. 전전전(n-3)까지의 최대 양 + 전(n-1)번째 양 + 현재 양 = (dp[n-3] + wine[n-1] + wine[n])

두가지 경우 중 더 큰 수를 dp에 저장하는 방식입니다.

이렇게 되면 문제에서 제시한 기본 예시 데이터만으로도 문제 파악이 가능합니다.

문제에서는 6잔에 6 10 13 9 8 1을 제시했으며 이 입력일 때 최종 dp에 저장된 값들을 살펴보면 됩니다.

최종 저장된 dp 값을 살펴보면 [6 16 23 28 33 32] 입니다. 여기서 마지막 32가 문제라는 것을 확인 가능합니다. dp[6]에 저장되어야 하는 값은 32가 아니라 33입니다.
32가 저장된 이유는 현재(n) 와인을 마시지 않는 경우를 고려하지 않았기 때문입니다. dp[n-1]에 해당하는 33과 비교를 하지 않았죠.
이러면 33이 저장되어야 하는데 32가 저장됐으므로 뒤에 추가 데이터가 있을 경우 계산 중 문제가 발생할 수 있는 여지가 당연히 있습니다.

예를들어 추가 데이터로 9잔, 6 10 13 9 8 1 1 2 4 라고 했을 때
기존 코드로는 dp 값이 [6 16 23 28 33 32 34 36 38] 이 됩니다. 문제가 생겼죠. 32가 아니라 33이 저장되어 33 + 2 + 4로 39가 되어야하는데 38이 결과로 나와버렸습니다.

그러니 기존 2가지 조건에 전(n-1)까지 최대 양 + 현재 와인을 마시지 않는 경우도 추가하여 같이 비교해주어야합니다.

==>
개선된 코드

import sys

n = int(sys.stdin.readline())

data = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0]*(n+1)
dp[1] = data[0]

if n >= 2:
    dp[2] = dp[1]+data[1]

for i in range(3, n+1):
    dp[i] = max(dp[i-2]+data[i-1], dp[i-3]+data[i-2]+data[i-1], dp[i-1])

print(dp[n])
"""
