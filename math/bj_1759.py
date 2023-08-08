"""
암호 만들기
"""

from itertools import combinations

vowel = ['a', 'e', 'i', 'o', 'u']

l, c = map(int, input().split())
array = list(input().split())
array.sort()

for word in combinations(array, l):
    count_vowel = 0
    for letter in word:
        if letter in vowel:
            count_vowel += 1

    if count_vowel >= 1 and l - count_vowel >= 2:
        print("".join(word))
