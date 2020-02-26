def check(x,y):
    cnt_x = 0
    cnt_y = 0
    for b in range(y,N):
        if base[x][b]==0:
            break
        cnt_y += 1
    for a in range(x,N):
        if base[a][y]==0:
            break
        cnt_x += 1
    for a in range(x,x+cnt_x):
        for b in range(y,y+cnt_y):
            visit[a][b] = 1
    return cnt_x, cnt_y

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    base = [list(map(int,input().split()))for _ in range(N)]
    visit = [[0 for _ in range(N)]for _ in range(N)]

    result = []
    for i in range(N):
        for j in range(N):
            if base[i][j]!=0 and visit[i][j]==0:
                result.append(tuple(check(i,j)))
    
    cnt = len(result)
    for i in range(cnt-1,0,-1):
        for j in range(0,i):
            if result[j][0]*result[j][1]>result[j+1][0]*result[j+1][1]:
                result[j], result[j+1] = result[j+1],result[j]
            elif result[j][0]*result[j][1]==result[j+1][0]*result[j+1][1]:
                if result[j][0]>result[j+1][0]:
                    result[j], result[j+1] = result[j+1], result[j]
    s = str(cnt)

    for i in result:
        s += ' '
        s += str(i[0])
        s += ' '
        s += str(i[1])

    print('#{} {}'.format(tc,s))