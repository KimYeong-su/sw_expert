def find(r,c):
    pass

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    mountain = [list(map(int,input().split()))for _ in range()]

    top = 0
    start = []
    maximum = 0
    for i in range(len(N)):
        for j in range(len(N)):
            if mountain[i][j]>maximum:
                maximum = mountain[i][j]
    for i in range(len(N)):
        for j in range(len(N)):
            if mountain[i][j]==maximum:
                start.append((i,j))

    result = 0
    for i in range(len(start)):
        row, col = start[i]
        if find(row,col)>result:
            result = find(row,col)

    print('#{} {}'.format(tc, result))