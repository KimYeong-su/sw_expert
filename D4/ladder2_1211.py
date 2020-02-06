for case in range(10):
    n = int(input())
    base = []

    for i in range(100):
        base.append(list(map(int,input().split())))
    mini = 400
    result = []
    for i in range(100):
        j = 0
        d = i
        cnt = 0
        if base[j][d] == 1:
            result.append(d)
            while j != 99:
                if  0<=d<99 and base[j][d+1]==1:
                    base[j][d] = 2
                    d += 1
                    cnt += 1
                elif 0<d<=99 and base[j][d-1]==1:
                    base[j][d] = 2
                    d -= 1
                    cnt += 1
                else:
                    base[j][d] = 2
                    j += 1
                    cnt += 1
            result.append(cnt)    
            if mini > cnt:
                mini = cnt
        for x in range(100):
            for y in range(100):
                if base[x][y] == 2:
                    base[x][y] = 1
                
    final = result[result.index(mini)-1]
    print(f'#{case+1} {final}')