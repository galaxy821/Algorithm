"""
주차 요금 계산 [https://school.programmers.co.kr/tryouts/72131/challenges?language=python3]
"""


def convert_data(time):
    h, m = time.split(":")
    return 60*int(h) + int(m)


def solution(fees, records):
    answer = []
    current = {}
    results = {}

    for record in records:
        tim, car, typ = record.split()

        if typ == "IN":
            current[car] = convert_data(tim)
        else:
            results[car] = (results.get(car, 0) +
                            convert_data(tim)-current[car])
            del current[car]

    for car, tim in current.items():
        results[car] = (results.get(car, 0) +
                        convert_data("23:59")-current[car])

    results = sorted(results.items(), key=lambda x: int(x[0]))

    for _, result in results:
        if result <= fees[0]:
            answer.append(fees[1])
        else:
            n, d = divmod((result-fees[0]), fees[2])
            if d > 0:
                n += 1
            answer.append(fees[1] + n * fees[3])

    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
      "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))  # 14600, 34400, 5000]
