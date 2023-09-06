"""
스택 [https://www.acmicpc.net/problem/10828]
"""

"""
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

import sys
from collections import deque
n = int(sys.stdin.readline())
data = deque()
for _ in range(n):
    command = sys.stdin.readline().strip()

    if "top" == command:
        print(data[len(data)-1] if len(data) != 0 else -1, end="\n")
    elif "size" == command:
        print(len(data), end="\n")
    elif "empty" == command:
        print(1 if len(data) == 0 else 0, end="\n")
    elif "pop" == command:
        print(data.pop() if len(data) != 0 else -1)
    else:
        _, num = command.split(" ")
        data.append(num)
