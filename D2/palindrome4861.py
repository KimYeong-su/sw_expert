T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    base = [list(input()) for _ in range(N)]
    base_r = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            if base[i][j:j+M]==list(reversed(base[i][j:j+M])):
                print('#{} {}'.format(tc,''.join(base[i][j:j+M])))
                break

    for i in range(N):
        for j in range(N):
            base_r[i][j] = base[N-1-j][i]
    
    for i in range(N):
        for j in range(N-M+1):
            if base_r[i][j:j+M]==list(reversed(base_r[i][j:j+M])):
                print('#{} {}'.format(tc,''.join(base_r[i][j:j+M])))
                break