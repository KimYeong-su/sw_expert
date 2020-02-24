def check(x,y):
    dx = [1,1,-1,-1]
    dy = [1,-1,-1,1]
    visit = [[0 for _ in range(N)]for _ in range(N)]
    history = [base[x][y]]
    cnt = 1
    px = x
    py = y

    for i in range(4):
        while True:
            nx = px + dx[i]
            ny = py + dy[i]
            if 0<=nx<N and 0<=ny<N and base[nx][ny] not in history and visit[nx][ny]==0:
                    cnt+=1
                    px,py = nx,ny
                    visit[nx][ny] = cnt
                    history.append(base[nx][ny])
            else:
                break
    if px == x+1 and py == y-1:
        return cnt
    else:
        return -1


T = int(input())
for tc in range(1,T+1):
    N = int(input())

    base = [list(map(int,input().split()))for _ in range(N)]
    maximum = -1
    for i in range(N):
        for j in range(N):
            result=check(i,j)
            if maximum<result:
                maximum = result

    print('#{} {}'.format(tc,maximum))