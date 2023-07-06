"""
크로아티아 알파벳 [https://www.acmicpc.net/problem/2941]
"""

value = input()

alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
i = 0
while True:
    if i >= len(value):
        break
    if value[i: i+2] in alphabet:
        count += 1
        i += 2
    elif value[i: i+3] in alphabet:
        count += 1
        i += 3
    else:
        count += 1
        i += 1
print(count)
