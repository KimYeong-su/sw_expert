def find(row,col,space,cnt,K):
    global maximum
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    if maximum < cnt:
        maximum = cnt

    visit[row][col] = 1
    for a in range(4):
        nr = row + dx[a]
        nc = col + dy[a]
        if 0<=nr<N and 0<=nc<N and visit[nr][nc]==0:
            if space!=0:
                if base[nr][nc] < base[row][col]:
                    find(nr,nc,space,cnt+1,K)
                if space!=-1:
                    for k in range(1,K+1):
                        if base[nr][nc]-k < base[row][col]:
                            find(nr,nc,0,cnt+1,k)
            else:
                if base[nr][nc] < base[row][col]-K:
                    find(nr,nc,-1,cnt+1,K)
    visit[row][col] = 0


T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())

    base = [list(map(int,input().split()))for _ in range(N)]
    visit = [[0 for _ in range(N)]for _ in range(N)]

    maximum = 0
    high = 0
    for i in base:
        if high < max(i):
            high = max(i)

    for i in range(N):
        for j in range(N):
            if base[i][j]==high:
                find(i,j,1,1,K)
    print('#{} {}'.format(tc,maximum))