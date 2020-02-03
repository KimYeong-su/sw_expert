def Wall(x, y):
    if x < 0 or x >= N:
        return True
    if y < 0 or y >= N:
        return True
    return False

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for case in range(1, int(input())+1):
    N = int(input())
    val = 0
    x, y = 0, -1
    Array = [[0 for x in range(N)]for y in range(N)]
    while val < N*N:
        for i in range(4):
            while True:
                nx = x+dx[i]
                ny = y+dy[i]
                if Wall(nx, ny):
                    break
                if Array[nx][ny] != 0 and val > Array[nx][ny]:
                    break
                val += 1
                Array[nx][ny] = val
                x = nx
                y = ny

    print('#{}'.format(case))
    for i in Array:
        print('{}'.format( ' '.join(list(map(str, i)))))