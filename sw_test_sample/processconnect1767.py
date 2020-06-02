'''
크루스칼로 구현
'''
import heapq

dx = [0,0,1,-1]
dy = [1,-1,0,0]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maxinos=[]
    for _ in range(N):
        maxinos.append(list(map(int,input().split())))
    pq = []
    for i in range(N):
        for j in range(N):
            if maxinos[i][j]==1 and 0<i<N-1 and 0<j<N-1:
                for k in range(4):
                    cnt = 0
                    x = i + dx[k]
                    y = j + dy[k]
                    while 0<=x<N and 0<=y<N:
                        if maxinos[x][y]:
                            cnt=0
                            break
                        cnt+=1
                        x = x + dx[k]
                        y = y + dy[k]
                    if cnt!=0:
                        heapq.heappush(pq,(cnt,i,j,k))
    while len(pq):
        print(heapq.heappop(pq))
                    
    
