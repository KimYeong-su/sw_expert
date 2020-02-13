def pipe(r,c,time):
    dx = [-1,1,0,0] # 위, 아래, 좌, 우
    dy = [0,0,-1,1]
    check_arr = [[0 for _ in range(M)]for _ in range(N)]
    check_arr[r][c]=1
    history=[(r,c)]
    t=1
    cnt=1
    while t<time:
        for index in range(len(history)):
            pr,pc=history.pop(0)
            if base[pr][pc]==1:
                for i in range(4):
                    nr = pr+dx[i]
                    nc = pc+dy[i]
                    if N>nr>=0 and 0<=nc<M and check_arr[nr][nc]==0:
                        if i == 0:
                            if base[nr][nc] == 1 or base[nr][nc] == 2 or base[nr][nc] == 5 or base[nr][nc] == 6:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
                        elif i==1:
                            if base[nr][nc] == 1 or base[nr][nc] == 2 or base[nr][nc] == 4 or base[nr][nc] == 7:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
                        elif i==2:
                            if base[nr][nc] == 1 or base[nr][nc] == 3 or base[nr][nc] == 4 or base[nr][nc] == 5:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
                        else:
                            if base[nr][nc] == 1 or base[nr][nc] == 3 or base[nr][nc] == 6 or base[nr][nc] == 7:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
            elif base[pr][pc]==2:
                for i in range(2):
                    nr = pr+dx[i]
                    nc = pc+dy[i]
                    if N>nr>=0 and 0<=nc<M and check_arr[nr][nc]==0:
                        if i==0:
                            if base[nr][nc] == 1 or base[nr][nc] == 2 or base[nr][nc] == 5 or base[nr][nc] == 6:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
                        else:
                            if base[nr][nc] == 1 or base[nr][nc] == 2 or base[nr][nc] == 4 or base[nr][nc] == 7:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
            elif base[pr][pc]==3:
                for i in range(2,4):
                    nr = pr+dx[i]
                    nc = pc+dy[i]
                    if N>nr>=0 and 0<=nc<M and check_arr[nr][nc]==0:
                        if i==2:
                            if base[nr][nc] == 1 or base[nr][nc] == 3 or base[nr][nc] == 4 or base[nr][nc] == 5:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
                        else:
                            if base[nr][nc] == 1 or base[nr][nc] == 3 or base[nr][nc] == 6 or base[nr][nc] == 7:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
            elif base[pr][pc]==4:
                for i in range(0,4,3):
                    nr = pr+dx[i]
                    nc = pc+dy[i]
                    if N>nr>=0 and 0<=nc<M and check_arr[nr][nc]==0:
                        if i==0:
                            if base[nr][nc] == 1 or base[nr][nc] == 2 or base[nr][nc] == 5 or base[nr][nc] == 6:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
                        else:
                            if base[nr][nc] == 1 or base[nr][nc] == 3 or base[nr][nc] == 6 or base[nr][nc] == 7:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
            elif base[pr][pc]==5:
                for i in range(1,4,2):
                    nr = pr+dx[i]
                    nc = pc+dy[i]
                    if N>nr>=0 and 0<=nc<M and check_arr[nr][nc]==0:
                        if i==1:
                            if base[nr][nc] == 1 or base[nr][nc] == 2 or base[nr][nc] == 4 or base[nr][nc] == 7:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
                        else:
                            if base[nr][nc] == 1 or base[nr][nc] == 3 or base[nr][nc] == 6 or base[nr][nc] == 7:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
            elif base[pr][pc]==6:
                for i in range(1,3):
                    nr = pr+dx[i]
                    nc = pc+dy[i]
                    if N>nr>=0 and 0<=nc<M and check_arr[nr][nc]==0:
                        if i==1:
                            if base[nr][nc] == 1 or base[nr][nc] == 2 or base[nr][nc] == 4 or base[nr][nc] == 7:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
                        else:
                            if base[nr][nc] == 1 or base[nr][nc] == 3 or base[nr][nc] == 4 or base[nr][nc] == 5:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
            else:
                for i in range(0,4,2):
                    nr = pr+dx[i]
                    nc = pc+dy[i]
                    if N>nr>=0 and 0<=nc<M and check_arr[nr][nc]==0:
                        if i==0:
                            if base[nr][nc] == 1 or base[nr][nc] == 2 or base[nr][nc] == 5 or base[nr][nc] == 6:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
                        else:
                            if base[nr][nc] == 1 or base[nr][nc] == 3 or base[nr][nc] == 4 or base[nr][nc] == 5:
                                check_arr[nr][nc]=1
                                history.append((nr,nc))
                                cnt+=1
        t+=1
    return cnt 
                                                        


T = int(input())

for tc in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    base = [list(map(int,input().split())) for _ in range(N)]

    result = pipe(R,C,L)
    print('#{} {}'.format(tc,result))