T = int(input())

for tc in range(1,T+1):
    base = [[0 for _ in range(500)]for _ in range(500)]
    flag = [[0 for _ in range(500)]for _ in range(500)]
    N,M,K = map(int,input().split()) # N 초기 세로, M 초기 가로, K 시간

    first = [list(map(int,input().split()))for _ in range(N)]
    row = int((500-N)/2)
    col = int((500-M)/2)
    # flag => 비활성 : 1, 활성 : 2, 죽은 : 3
    queue = []
    queue1 = []
    for i in range(N):
        for j in range(M):
            if first[i][j] != 0:
                base[row+i][col+j] = first[i][j]
                flag[row+i][col+j] = 1
                queue.append((row+i,col+j))
                queue1.append((0,first[i][j]))

    time = 1
    while time<=K:
        temp = []
        temp1 = []
        while len(queue)!=0:
            x,y = queue.pop(0)
            cnt,life = queue1.pop(0)
            dx = [1,-1,0,0]
            dy = [0,0,1,-1]

            if flag[x][y]==1:
                if time-cnt==base[x][y]:
                    flag[x][y]=2
                temp.append((x,y))
                temp1.append((cnt,life))
            elif flag[x][y]==2:
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if flag[nx][ny]==0:
                        flag[nx][ny]=1
                        base[nx][ny]=base[x][y]
                        temp.append((nx,ny))
                        temp1.append((time,base[x][y]))
                    elif flag[nx][ny]==1:
                        if (nx,ny) in temp:
                            index = temp.index((nx,ny))
                            if temp1[index][1]<base[x][y] and temp1[index][0]==time:
                                base[nx][ny]=base[x][y]
                                temp1[index] = (time,base[x][y])
                if life==1:
                    flag[x][y]=3
                elif life>1:
                    temp.append((x,y))
                    temp1.append((time,life-1))
        for a in temp:
            queue.append(a)
        for a in temp1:
            queue1.append(a)
        time +=1
    result = 0
    for cnt in flag:
        result += cnt.count(1)
        result += cnt.count(2)

    print('#{} {}'.format(tc,result))