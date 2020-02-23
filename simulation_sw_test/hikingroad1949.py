def find(r,c,d):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    case = 0
    stack = [(r,c,d,1)]
    history = []
    while len(stack)!=0:
        pr,pc,pd,temp = stack.pop()
        history.append((pr,pc))
        l = len(history)
        for i in range(4):
            nr = pr + dx[i]
            nc = pc + dy[i]
            if 0<=nr<N and 0<=nc<N:
                if pd==0 and (nr,nc) not in history:
                    if mountain[nr][nc]<mountain[pr][pc]-K:
                        stack.append((nr,nc,-1,temp+1))
                elif pd==-1 and (nr,nc) not in history:
                    if mountain[nr][nc]<mountain[pr][pc]:
                        stack.append((nr,nc,-1,temp+1))
                elif pd==d and (nr,nc) not in history:
                    if mountain[nr][nc]<mountain[pr][pc]:
                        stack.append((nr,nc,pd,temp+1))
                    if mountain[nr][nc]-pd<mountain[pr][pc]:
                        stack.append((nr,nc,0,temp+1))
        if l == len(history):
            history.pop()
        print(history)
        # print(stack)
        if case < temp:
            case = temp
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
    # print(start)
    result = 0
    for i in range(len(start)):
        row, col = start[i]
        if find(row,col,K)>result:
            result = find(row,col,K)

    print('#{} {}'.format(tc, result))