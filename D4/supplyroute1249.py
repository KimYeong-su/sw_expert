import heapq

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def Dijkstra():
    while True:
        k,x,y=heapq.heappop(pq)
        if visit[x][y]: continue
        visit[x][y]=True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                key[nx][ny] = min(key[nx][ny], k+base[nx][ny])
                if nx==N-1 and ny==N-1:
                    return key[N-1][N-1]
                heapq.heappush(pq,[key[nx][ny],nx,ny])


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    base = []
    for _ in range(N):
        base.append(list(map(int,input())))

    pq = []
    heapq.heappush(pq,[base[0][0],0,0])
    
    key = [[float('inf')]*N for _ in range(N)]
    key[0][0]=0
    visit = [[False]*N for _ in range(N)]
    result=Dijkstra()
    # print(key)
    print('#{} {}'.format(tc,result))