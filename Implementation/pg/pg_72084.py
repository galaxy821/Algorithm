"""
오픈 채팅방 [https://school.programmers.co.kr/tryouts/72084/challenges?language=python3]
"""


def solution(records):
    user_name = {}
    result = []
    answer = []

    for record in records:
        if record[:5] == "Enter":
            op, uid, name = record.split()
            user_name[uid] = name
            result.append((uid, op))
        elif record[:5] == "Leave":
            op, uid = record.split()
            result.append((uid, op))
        elif record[:6] == "Change":
            op, uid, name = record.split()
            user_name[uid] = name

    for uid, op in result:
        if op == "Enter":
            answer.append(f"{user_name[uid]}님이 들어왔습니다.")
        elif op == "Leave":
            answer.append(f"{user_name[uid]}님이 나갔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
