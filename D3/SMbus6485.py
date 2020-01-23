a = int(input())

for l in range(a):
    ran = []
    stop = []
    result = []
    for i in range(int(input())):
        ran.append(tuple(map(int, input().split())))
    p = int(input())
    for k in range(p):
        stop.append(int(input()))
    for j in stop:
        cnt = 0
        for min, max in ran:
            if min <= j <= max:
                cnt+= 1
        result.append(cnt)
    print(f'#{l+1} {" ".join(map(str,result))}')