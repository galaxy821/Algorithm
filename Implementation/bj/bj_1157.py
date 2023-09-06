"""
단어 공부 [https://www.acmicpc.net/problem/1157]
"""

word = input().upper()

counter = {}

for letter in word:
    if letter in counter:
        counter[letter] += 1
    else:
        counter[letter] = 0

counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

if len(counter) > 1 and counter[0][1] == counter[1][1]:
    print("?")
else:
    print(counter[0][0])

# 다륹 풀이
"""
word = input().upper()
unique_letter = list(set(word))
counter = list()

for letter in unique_letter:
    counter.append(word.count(letter))

if counter.count(max(counter)) > 1:
    print("?")
else:
    max_index = counter.index(max(counter))
    print(unique_letter[max_index])
"""
