def check(row,col,cnt,ans):
    if cnt>5:
        result.add(ans)
        return

    for i in range(4):
        nx = row+dx[i]
        ny = col+dy[i]
        if 0<=nx<4 and 0<=ny<4:
            check(nx,ny,cnt+1,ans+base[nx][ny])


T = int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for tc in range(1,T+1):
    base = [list(map(str,input().split()))for _ in range(4)]

    result = set()
    for i in range(4):
        for j in range(4):
            check(i,j,0,base[i][j])

    print('#{} {}'.format(tc,len(result)))
