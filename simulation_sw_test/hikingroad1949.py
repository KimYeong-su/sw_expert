def find(r,c,d):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    cnt = 1
    case = 0
    stack = [(r,c,d)]
    while True:
        pr,pc,pd = stack.pop()
        for i in range(4):
            nr = pr + dx[i]
            nc = pc + dy[i]
            if 0<=nr<N and 0<=nc<N:
                if pd==0:
                    if mountain[nr][nc]<mountain[pr][pc]:
                        stack.append((nr,nc,pd))
                        cnt+=1
                    else:
                        cnt-=1
                else:
                    if mountain[nr][nc]<mountain[pr][pc]:
                        stack.append((nr,nc,pd))
                        cnt+=1
                    if mountain[nr][nc]<mountain[pr][pc]-pd:
                        stack.append((nr,nc,0))
                        cnt+=1
                    else:
                        cnt-=1
        if case < cnt:
            case = cnt
        if len(stack)==0:
            break
    return case

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    mountain = [list(map(int,input().split()))for _ in range(N)]

    top = 0
    start = []
    maximum = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j]>maximum:
                maximum = mountain[i][j]
    for i in range(N):
        for j in range(N):
            if mountain[i][j]==maximum:
                start.append((i,j))

    result = 0
    for i in range(len(start)):
        row, col = start[i]
        if find(row,col,K)>result:
            result = find(row,col,K)

    print('#{} {}'.format(tc, result))