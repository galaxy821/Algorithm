"""
팰린드롬수 [https://www.acmicpc.net/problem/1259]
"""

while True:
    value = input()
    if value == "0":
        break

    result = True
    for i in range(len(value)//2):
        if value[i] != value[-(i+1)]:
            result = False
            break

    if result:
        print("yes")
    else:
        print("no")
