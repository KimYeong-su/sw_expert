dx = [1,1,-1,-1]
dy = [1,-1,-1,1]
def check(row,col,cnt,visit,kind,start,index):
    global maximum
    if start==(row,col)and index==3:
        if maximum<cnt:
            maximum=cnt
    if maximum == 2*(N-1):
        return
    else:
        nx = row + dx[index]
        ny = col + dy[index]
        if 0<=nx<N and 0<=ny<N:
            if (nx,ny) not in visit and base[nx][ny] not in kind:
                visit.append((nx,ny))
                kind.append(base[nx][ny])
                check(nx,ny,cnt+1,visit,kind,start,index)
                if index+1<4:
                    check(nx,ny,cnt+1,visit,kind,start,index+1)
                visit.pop()
                kind.pop()


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    base = [list(map(int,input().split()))for _ in range(N)]
    maximum = -1
    for i in range(N):
        for j in range(N):
            if j != 0 and j!=N-1 and i!=N-1:
                check(i,j,0,[],[],(i,j),0)
    print('#{} {}'.format(tc,maximum))