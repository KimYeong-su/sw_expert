cases = int(input())

for case in range(cases):
    Time = int(input())
    v = 0
    s = 0
    for t in range(Time):
        temp = list(map(int, input().split()))
        if temp[0] == 1:
            v += temp[1]
        elif temp[0] == 2:
            if v-temp[1]<0:
                v = 0
            else:
                v -= temp[1]
        
        
        s += v

    print(f'#{case+1} {s}')