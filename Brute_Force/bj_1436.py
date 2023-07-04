n = int(input())

count = 0
cur_value = 666
while True:
    if '666' in str(cur_value):
        count += 1
        if count == n:
            break
    cur_value += 1

print(cur_value)
