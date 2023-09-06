"""
국영수 [https://www.acmicpc.net/problem/10825]
"""

import sys

n = int(sys.stdin.readline())
student_data = []

for _ in range(n):
    name, korean, english, math_ = sys.stdin.readline().split()
    student_data.append([name, int(korean), int(english), int(math_)])

student_data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(student_data[i][0], end="\n")
