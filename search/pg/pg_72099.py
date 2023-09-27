"""
가사 검색 [https://school.programmers.co.kr/tryouts/72099/challenges?language=python3]
"""

from bisect import bisect_left, bisect_right


def count_words(words, left_value, right_value):
    l_index = bisect_left(words, left_value)
    r_index = bisect_right(words, right_value)

    return r_index - l_index


def solution(words, queries):
    array = [[] for _ in range(10001)]
    r_array = [[] for _ in range(10001)]

    for word in words:
        array[len(word)].append(word)
        r_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        r_array[i].sort()

    answer = []
    for q in queries:
        if q[0] != "?":
            answer.append(count_words(
                array[len(q)], q.replace('?', 'a'), q.replace('?', 'z')))
        else:
            answer.append(count_words(r_array[len(q)], q[::-1].replace(
                '?', 'a'), q[::-1].replace('?', 'z')))

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], [
      "fro??", "????o", "fr???", "fro???", "pro?"]))  # [3, 2, 4, 1, 0]
