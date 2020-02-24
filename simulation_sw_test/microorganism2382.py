T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    
    order = [tuple(map(int,input().split()))for _ in range(K)]

    time = 0
    while time<M:
        dx = [0,-1,1,0,0]
        dy = [0,0,0,-1,1]
        temp1 = [[0 for _ in range(N)]for _ in range(N)] #방향성
        temp2 = [[0 for _ in range(N)]for _ in range(N)] #갯수
        temp3 = [[0 for _ in range(N)]for _ in range(N)] #방향성을 위한 갯수
        while len(order)!=0:
            x, y, num, direction = order.pop(0)
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx==0 or nx==N-1 or ny==0 or ny==N-1:
                if num//2!=0:
                    temp2[nx][ny] = num//2
                    if direction==1:
                        temp1[nx][ny]=2
                    elif direction==2:
                        temp1[nx][ny]=1
                    elif direction==3:
                        temp1[nx][ny]=4
                    elif direction==4:
                        temp1[nx][ny]=3
            else:
                temp2[nx][ny] += num
                if temp3 == 0:
                    temp3[nx][ny] = num
                    temp1[nx][ny] = direction
                else:
                    if temp3[nx][ny] < num:
                        temp3[nx][ny] = num
                        temp1[nx][ny] = direction
        for i in range(N):
            for j in range(N):
                if temp2[i][j]!=0:
                    order.append((i,j,temp2[i][j],temp1[i][j]))
        time +=1

    result = 0
    for i in order:
        result += i[2]

    print('#{} {}'.format(tc,result))