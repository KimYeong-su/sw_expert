T = int(input())

def dfs(row, col, tmp):
    global case
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    if len(tmp) == 7:
        if tmp in case: return
        case.append(tmp)
        return
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0<=nr<4 and 0<=nc<4:
            dfs(nr, nc, tmp+str(grid[nr][nc]))



for tc in range(1,T+1):
    grid = [list(map(int, input().split())) for _ in range(4)]
    case = []
    for i in range(4):
        for j in range(4):
            dfs(i,j,str(grid[i][j]))
    print(f'#{tc} {len(case)}')