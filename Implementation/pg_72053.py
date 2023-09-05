"""
이상한 문자 만들기 [https://school.programmers.co.kr/tryouts/72053/challenges?language=python3]
"""

# 원래는 str와 ord로 해결하려고 했는데 왜 안되는지 아직 파악하지 못함
# 그래서 upper()와 lower() 함수로 해결함


def solution(s):
    words = s.split(" ")
    result = []
    for word in words:
        temp = ""
        for i in range(len(word)):
            if i % 2 == 0:

                if "a" <= word[i] <= "z":
                    temp += word[i].upper()
                else:
                    temp += word[i]
            else:
                if 'A' <= word[i] <= 'Z':
                    temp += word[i].lower()
                else:
                    temp += word[i]
        result.append(temp)

    answer = " ".join(result)
    return answer


print(solution("try hello world"))
