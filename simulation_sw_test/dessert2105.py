def check(x,y,cnt):
    global maximum
    dx = [1,1,-1,-1]
    dy = [1,-1,-1,1]
    px, py = x, y

    history.append(base[x][y])
    visit[x][y]=1
    for i in range(4):
        nx = px + dx[i]
        ny = py + dy[i]
        if 0<=nx<N and 0<=ny<N and base[nx][ny] not in history and visit[nx][ny]==0:
            print(history)
            if nx==i and ny==j:
                if maximum < cnt+1:
                    maximum = cnt+1
            check(nx,ny,cnt+1)
    visit[x][y]=0
    history.pop()
        


T = int(input())
for tc in range(1,T+1):
    N = int(input())

    visit = [[0 for _ in range(N)]for _ in range(N)]
    history = []
    base = [list(map(int,input().split()))for _ in range(N)]
    maximum = -1
    for i in range(N):
        for j in range(N):
            check(i,j,0)

    print('#{} {}'.format(tc,maximum))