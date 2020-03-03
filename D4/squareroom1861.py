def room(row, col, cnt):
    global maximum, flag
    if maximum < cnt:
        maximum=cnt
        flag=2
    elif maximum == cnt:
        flag = 1
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(4):
        nx = row+dx[i]
        ny = col+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if base[row][col]+1==base[nx][ny]:
                room(nx,ny,cnt+1)

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    base=[list(map(int,input().split()))for _ in range(N)]
    maximum = 0
    number = 1000000
    for i in range(N):
        for j in range(N):
            flag=0
            room(i,j,1)
            if flag == 1:
                if number>base[i][j]:
                    number=base[i][j]
            elif flag == 2:
                number=base[i][j]
            # print(number,maximum)
    print('#{} {} {}'.format(tc,number,maximum)) 