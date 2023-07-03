"""
최대공약수와 최소공배수 [https://www.acmicpc.net/problem/2609]
"""
import math
a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))

# 다른 풀이
"""
def gcd_two_number(a, b):
    if b == 0:
        return a
    if a % b == 0:
        return b
    return gcd_two_number(b, a % b)


a, b = map(int, input().split())

if b > a:
    a, b = b, a

gcd_value = gcd_two_number(a, b)
print(gcd_value)
print(int(a*b/gcd_value))
"""
