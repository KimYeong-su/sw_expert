def bfs(start):
    queue = [start]
    maze[start[0]][start[1]] = 1
    dr = [0,0,-1,1]
    dc = [1,-1,0,0]

    while queue:
        row, col = queue.pop(0)
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0<=nr<100 and 0<=nc<100 and maze[nr][nc] != 1:
                if maze[nr][nc] == 3:
                    return 1
                maze[nr][nc] = 1
                queue.append((nr,nc))
    return 0

for _ in range(10):
    tc = int(input())
    maze = [list(map(int,input()))for _ in range(100)]
    start = -1
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                start = (i,j)
            if start != -1:
                break
    print(f'#{tc} {bfs(start)}')