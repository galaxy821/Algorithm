"""
전화번호 목록 [https://school.programmers.co.kr/tryouts/72082/challenges]
"""


def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book)-1):
        # if phone_book[i] in phone_book[i+1] : 부분일치로 예외케이스가 있음
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            break

    return answer


print(solution(["119", "97674223", "1195524421"]))
