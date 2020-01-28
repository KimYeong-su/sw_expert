cases = int(input())

for case in range(cases):
    hour1, minute1, hour2, minute2 = map(int, input().split())
    hour = hour1 + hour2
    minute = minute1 + minute2

    if minute >= 60:
        hour += minute//60
        minute = minute%60

    if hour >12:
        if hour % 12 ==0:
            hour = 12
        else:
            hour = hour%12

    print(f'#{case+1} {hour} {minute}')